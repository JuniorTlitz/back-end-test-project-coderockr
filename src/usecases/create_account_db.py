from abc import ABC, abstractmethod
from typing import Awaitable

from src.models.create_account_db_model import CreateAccountDbModel


class CreateAccountDb(ABC):
    @abstractmethod
    async def create_account(self, account: CreateAccountDbModel) -> Awaitable[bool]:
        pass
