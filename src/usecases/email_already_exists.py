from abc import ABC, abstractmethod
from typing import Awaitable


class EmailAlreadyExists(ABC):
    @abstractmethod
    async def validate_email(self, email: str):
        pass
