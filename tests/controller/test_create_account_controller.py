import pytest
from http import HTTPStatus
from unittest.mock import AsyncMock, Mock
from src.controller.create_account_controller import (
    CreateAccountController,
    EmailAlreadyExists,
)
from src.usecases.authentication import Authentication
from src.usecases.create_account_db import CreateAccountDb


@pytest.mark.asyncio
async def test_should_return_forbidden_if_email_already_exists():
    email_already_exists_mock = AsyncMock(spec=EmailAlreadyExists)
    email_already_exists_mock.validate_email.return_value = True

    create_account_db_mock = AsyncMock(spec=CreateAccountDb)
    create_account_db_mock.create_account.return_value = True

    authentication_mock = AsyncMock(spec=Authentication)
    sut = CreateAccountController(
        email_already_exists_mock, create_account_db_mock, authentication_mock
    )

    request = {
        "name": "any_name",
        "email": "any_email@email.com",
        "password": "any_password",
    }
    response = await sut.handle(request)

    assert response["status_code"] == HTTPStatus.FORBIDDEN
    assert response["message"] == "Account already exists"


@pytest.mark.asyncio
async def test_should_return_internal_server_error_if_account_creation_fails():
    email_already_exists_mock = AsyncMock(spec=EmailAlreadyExists)
    email_already_exists_mock.validate_email.return_value = False

    create_account_db_mock = AsyncMock(spec=CreateAccountDb)
    create_account_db_mock.create_account.return_value = False

    authentication_mock = AsyncMock(spec=Authentication)

    sut = CreateAccountController(
        email_already_exists_mock, create_account_db_mock, authentication_mock
    )

    request = {
        "name": "any_name",
        "email": "any_email@email.com",
        "password": "any_password",
    }
    response = await sut.handle(request)

    assert response["status_code"] == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response["message"] == "Internal server error"


@pytest.mark.asyncio
async def test_should_return_created_if_account_creation_succeeds():
    email_already_exists_mock = AsyncMock(spec=EmailAlreadyExists)
    email_already_exists_mock.validate_email.return_value = False

    create_account_db_mock = AsyncMock(spec=CreateAccountDb)
    create_account_db_mock.create_account.return_value = True

    authentication_mock = AsyncMock(spec=Authentication)
    authentication_mock.auth.return_value = {"token": "any_token"}

    sut = CreateAccountController(
        email_already_exists_mock, create_account_db_mock, authentication_mock
    )

    request = {
        "name": "any_name",
        "email": "any_email@email.com",
        "password": "any_password",
    }
    response = await sut.handle(request)

    assert response["status_code"] == HTTPStatus.CREATED
    assert response["body"] == {"token": "any_token"}
