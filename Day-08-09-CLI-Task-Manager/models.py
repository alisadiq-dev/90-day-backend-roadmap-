from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    status: str = "pending"
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    note: Optional[str] = None

    # === for print ===

    def __str__(self):
        status_emoji = "✅" if self.status == "completed" else "⏳"
        return f"{self.id}. {status_emoji} {self.title}"
 