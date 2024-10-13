from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class Category:
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: datetime = field(default_factory=datetime.now)

