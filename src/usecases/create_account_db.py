from abc import ABC, abstractmethod

from src.models.create_account_db_model import CreateAccountDbModel


class CreateAccountDb(ABC):
    @abstractmethod
    def create_account(self, account: CreateAccountDbModel):
        pass
