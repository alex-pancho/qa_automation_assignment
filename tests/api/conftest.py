import pytest
from api.endpoints.json_placeholder import Default
from framework_api.config import ConfigManager
from framework_api.client import ApiClient

@pytest.fixture(scope="session")
def manager() -> ConfigManager:
    conf = "test"
    return ConfigManager(f"./configs/{conf}.yaml")


@pytest.fixture(scope="session")
def host(manager: ConfigManager) -> str:
    host = f"https://{manager.config.api.base_portal}"
    return host


@pytest.fixture(scope="session")
def api_client(host):
    return ApiClient


@pytest.fixture(scope="session")
def default():
    return Default()
