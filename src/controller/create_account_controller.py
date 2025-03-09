from abc import ABC, abstractmethod
from http import HTTPStatus
from typing import Any


class EmailAlreadyExists(ABC):
    @abstractmethod
    def validate_email(self, email: str) -> bool:
        pass

class CreateAccountController:
    def __init__(self, email_already_exists: EmailAlreadyExists):
        self._email_already_exists = email_already_exists

    async def handle(self, request):
        is_valid = self._email_already_exists.validate_email(request['email'])

        if is_valid:
            return {'status_code': HTTPStatus.FORBIDDEN, 'message': 'Account already exists'}