from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Endpoint:
    """
    Endpoint definition with method, path and optional body.
    """
    method: str
    endpoint: str
    body: Dict[str, Any] = field(default_factory=dict)
