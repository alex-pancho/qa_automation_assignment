import logging
from functools import wraps
from typing import Callable


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Setup logger instance"""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger


def log_action(action_name: str) -> Callable:
    """Decorator for logging actions"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            logger = setup_logger(self.__class__.__name__)
            locator_info = getattr(self, "_locator", "unknown")
            logger.info(f"Starting: {action_name} on {locator_info}")
            try:
                result = func(self, *args, **kwargs)
                logger.info(f"{result}: {action_name}")
                return result
            except Exception as e:
                logger.error(
                    f"Failed: {action_name}. Error: {type(e).__name__}: {str(e)}"
                )
                raise

        return wrapper

    return decorator


def log_debug(msg: str = "") -> logging.Logger:
    logger = setup_logger("logger", logging.DEBUG)
    logger.debug(msg)


def log_info(msg: str = "") -> logging.Logger:
    logger = setup_logger("logger")
    logger.info(msg)


def log_waning(msg: str = "") -> logging.Logger:
    logger = setup_logger("logger")
    logger.warning(msg)


def log_error(msg: str = "") -> logging.Logger:
    logger = setup_logger("logger")
    logger.error(msg)
