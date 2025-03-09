from abc import ABC, abstractmethod


class EmailAlreadyExists(ABC):
    @abstractmethod
    def validate_email(self, email: str) -> bool:
        pass
