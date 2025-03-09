import pytest
from http import HTTPStatus
from unittest.mock import Mock
from src.controller.create_account_controller import CreateAccountController, EmailAlreadyExists

@pytest.mark.asyncio
async def test_should_return_forbidden_if_email_already_exists():
    email_already_exists_mock = Mock(spec=EmailAlreadyExists)
    email_already_exists_mock.validate_email.return_value = True

    sut = CreateAccountController(email_already_exists_mock)

    request = {
        "name": "any_name",
        "email": "any_email@email.com",
        "password": "any_password",
    }
    response = await sut.handle(request)

    assert response['status_code'] == HTTPStatus.FORBIDDEN
    assert response['message'] == 'Account already exists'
