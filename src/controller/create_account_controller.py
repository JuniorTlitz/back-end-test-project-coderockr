from abc import ABC, abstractmethod
from http import HTTPStatus
from pydantic import BaseModel

from src.models.authentication_model import AuthenticationModel
from src.models.create_account_db_model import CreateAccountDbModel
from src.usecases.authentication import Authentication
from src.usecases.create_account_db import CreateAccountDb
from src.usecases.email_already_exists import EmailAlreadyExists


class CreateAccountController:

    def __init__(
        self,
        email_already_exists: EmailAlreadyExists,
        create_account_db: CreateAccountDb,
        authentication: Authentication,
    ):
        self._email_already_exists = email_already_exists
        self._create_account_db = create_account_db
        self._authentication = authentication

    async def handle(self, request):
        email_exists = await self._email_already_exists.validate_email(request["email"])

        if email_exists:
            return {
                "status_code": HTTPStatus.FORBIDDEN,
                "message": "Account already exists",
            }

        account = await self._create_account_db.create_account(
            CreateAccountDbModel(
                name=request["name"],
                email=request["email"],
                password=request["password"],
            )
        )

        if not account:
            return {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR,
                "message": "Internal server error",
            }

        auth = await self._authentication.auth(
            AuthenticationModel(
                email=request["email"],
                password=request["password"],
            )
        )

        return {
            "status_code": HTTPStatus.CREATED,
            "body": auth,
        }
