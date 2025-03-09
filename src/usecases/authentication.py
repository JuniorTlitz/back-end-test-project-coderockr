from abc import ABC, abstractmethod
from typing import Awaitable

from src.models.authentication_model import (
    AuthenticationModel,
    AuthenticationResponseModel,
)


class Authentication(ABC):
    @abstractmethod
    async def auth(
        self, authentication_params: AuthenticationModel
    ) -> Awaitable[AuthenticationResponseModel]:
        pass
