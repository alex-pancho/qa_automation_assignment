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
    """Конфігурація API клієнта"""

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
    """Конфігурація тестів"""

    max_response_time: float = Field(default=5.0, gt=0)
    retry_count: int = Field(default=0, ge=0)
    retry_delay: float = Field(default=1.0, ge=0)
    log_level: str = Field(
        default="INFO", pattern="^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$"
    )


class ReportConfig(BaseModel):
    """Конфігурація звітів"""

    output_dir: str = Field(default="./reports")
    format: str = Field(default="json", pattern="^(json|html|xml)$")
    include_timestamps: bool = True
    include_request_details: bool = True
    include_response_body: bool = False


class EnvironmentConfig(BaseModel):
    """Конфігурація середовища"""

    name: str = Field(default="default")
    api: APIConfig
    test: TestConfig = Field(default_factory=TestConfig)
    report: ReportConfig = Field(default_factory=ReportConfig)
    variables: Dict[str, Any] = Field(default_factory=dict)


class ConfigManager:
    """Менеджер конфігурацій"""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self.config: Optional[EnvironmentConfig] = None

        if config_path:
            self.load_config(config_path)

    def load_config(self, path: str) -> EnvironmentConfig:
        """Завантажує конфігурацію з файлу"""
        config_file = Path(path)

        if not config_file.exists():
            raise FileNotFoundError(f"Config file not found: {path}")

        # Визначаємо формат файлу
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
        """Зберігає конфігурацію у файл"""
        config_file = Path(path)

        # Створюємо директорію якщо не існує
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
        """Повертає конфігурацію API"""
        if not self.config:
            raise ValueError("Config not loaded")
        return self.config.api

    def get_test_config(self) -> TestConfig:
        """Повертає конфігурацію тестів"""
        if not self.config:
            raise ValueError("Config not loaded")
        return self.config.test

    def get_report_config(self) -> ReportConfig:
        """Повертає конфігурацію звітів"""
        if not self.config:
            raise ValueError("Config not loaded")
        return self.config.report

    def get_variable(self, key: str, default: Any = None) -> Any:
        """Повертає змінну з конфігурації"""
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


# Приклад створення конфігурацій для різних середовищ
def create_configs():
    """Створює приклади конфігураційних файлів"""

    # Development конфігурація
    name = "test"
    # w_config = work_config(name)
    test_config = EnvironmentConfig(
        name=name,
        api=work_config("BASE_API_URL"),
        test=TestConfig(max_response_time=10.0, retry_count=1, log_level="DEBUG"),
        variables={
            "client_id": os.getenv(f"{name}_clientId"),
            "client_secret": os.getenv(f"{name}_clientSecret"),
        },
    )

    # Зберігаємо конфігурації
    manager = ConfigManager()

    Path("./configs").mkdir(exist_ok=True)

    suffix = "yaml"

    manager.save_config(f"./configs/test.{suffix}", test_config)

    print("✓ Конфігураційні файли створено:")
    print(f"  - ./configs/test.{suffix}")
    print(f"  - ./configs/preprod.{suffix}")
    print(f"  - ./configs/prod.{suffix}")
    return suffix


# Приклад використання
if __name__ == "__main__":
    # Створення прикладів конфігурацій
    suffix = create_configs()
    for conf in ["test"]: #, "preprod", "prod"
        # Завантаження конфігурації
        manager = ConfigManager(f"./configs/{conf}.{suffix}")

        print("\n" + "=" * 50)
        print(f"Перевірка завантаження конфігурації {conf}:")
        print("=" * 50)
        print(f"env: {manager.config.name}")
        print(f"agreement URL: {manager.config.api.base_portal}")
        print(f"Timeout: {manager.config.api.timeout}s")
        print(f"Max Response Time: {manager.config.test.max_response_time}s")
        print(f"Log Level: {manager.config.test.log_level}")
        print(f"Client ID: {manager.get_variable('client_id')}")
