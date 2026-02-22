"""
Config for API Testing Framework
"""

import os
import json
import yaml

from dotenv import load_dotenv
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict
from pathlib import Path

load_dotenv()


class APIConfig(BaseModel):
    """API client configuration"""

    base_portal: str
    timeout: int = Field(default=30, ge=1)
    verify_ssl: bool = True
    headers: Dict[str, str] = Field(default_factory=dict)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "base_portal": "",
                "timeout": 30,
                "verify_ssl": True,
                "headers": {"Content-Type": "application/json"},
            }
        }
    )


class TestConfig(BaseModel):
    """Test configuration"""

    max_response_time: float = Field(default=5.0, gt=0)
    retry_count: int = Field(default=0, ge=0)
    retry_delay: float = Field(default=1.0, ge=0)
    log_level: str = Field(
        default="INFO", pattern="^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$"
    )


class ReportConfig(BaseModel):
    """Report configuration"""

    output_dir: str = Field(default="./reports")
    format: str = Field(default="json", pattern="^(json|html|xml)$")
    include_timestamps: bool = True
    include_request_details: bool = True
    include_response_body: bool = False


class EnvironmentConfig(BaseModel):
    """Environment configuration"""

    name: str = Field(default="default")
    api: APIConfig
    test: TestConfig = Field(default_factory=TestConfig)
    report: ReportConfig = Field(default_factory=ReportConfig)
    variables: Dict[str, Any] = Field(default_factory=dict)


class ConfigManager:
    """Configuration manager"""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self.config: Optional[EnvironmentConfig] = None

        if config_path:
            self.load_config(config_path)

    def load_config(self, path: str) -> EnvironmentConfig:
        """Loads configuration from file"""
        config_file = Path(path)

        if not config_file.exists():
            raise FileNotFoundError(f"Config file not found: {path}")

        # Detect file format
        if config_file.suffix == ".json":
            with open(config_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        elif config_file.suffix in [".yaml", ".yml"]:
            with open(config_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        else:
            raise ValueError(f"Unsupported config format: {config_file.suffix}")

        self.config = EnvironmentConfig(**data)
        return self.config

    def save_config(self, path: str, config: EnvironmentConfig):
        """Saves configuration to file"""
        config_file = Path(path)

        # Create directory if it does not exist
        config_file.parent.mkdir(parents=True, exist_ok=True)

        data = config.model_dump()

        if config_file.suffix == ".json":
            with open(config_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        elif config_file.suffix in [".yaml", ".yml"]:
            with open(config_file, "w", encoding="utf-8") as f:
                yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
        else:
            raise ValueError(f"Unsupported config format: {config_file.suffix}")

    def get_api_config(self) -> APIConfig:
        """Returns API configuration"""
        if not self.config:
            raise ValueError("Config not loaded")
        return self.config.api

    def get_test_config(self) -> TestConfig:
        """Returns test configuration"""
        if not self.config:
            raise ValueError("Config not loaded")
        return self.config.test

    def get_report_config(self) -> ReportConfig:
        """Returns report configuration"""
        if not self.config:
            raise ValueError("Config not loaded")
        return self.config.report

    def get_variable(self, key: str, default: Any = None) -> Any:
        """Returns variable from configuration"""
        if not self.config:
            raise ValueError("Config not loaded")
        return self.config.variables.get(key, default)


def work_config(name: str):
    return APIConfig(
        base_portal=os.getenv(f"{name}", "127.0.0.1:8000"),
        timeout=10,
        verify_ssl=False,
        headers={
            "Content-Type": "application/json",
            "X-Environment": "development",
        },
    )


# Example of creating configurations for different environments
def create_configs():
    """Creates example configuration files"""

    # Development configuration
    name = "test"
    test_config = EnvironmentConfig(
        name=name,
        api=work_config("BASE_API_URL"),
        test=TestConfig(max_response_time=10.0, retry_count=1, log_level="DEBUG"),
        variables={
            "client_id": os.getenv(f"{name}_clientId"),
            "client_secret": os.getenv(f"{name}_clientSecret"),
        },
    )

    # Save configurations
    manager = ConfigManager()

    Path("./configs").mkdir(exist_ok=True)

    suffix = "yaml"

    manager.save_config(f"./configs/test.{suffix}", test_config)

    print("✓ Configuration files created:")
    print(f"  - ./configs/test.{suffix}")
    return suffix


# Usage example
if __name__ == "__main__":
    # Create example configurations
    suffix = create_configs()
    for conf in ["test"]:  # , "preprod", "prod"
        # Load configuration
        manager = ConfigManager(f"./configs/{conf}.{suffix}")

        print("\n" + "=" * 50)
        print(f"Configuration load check: {conf}")
        print("=" * 50)
        print(f"env: {manager.config.name}")
        print(f"Base API URL: {manager.config.api.base_portal}")
        print(f"Timeout: {manager.config.api.timeout}s")
        print(f"Max Response Time: {manager.config.test.max_response_time}s")
        print(f"Log Level: {manager.config.test.log_level}")
        print(f"Client ID: {manager.get_variable('client_id')}")