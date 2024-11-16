from typing import Any

from fastapi import HTTPException


class SpyCatNotFound(HTTPException):
    def __init__(self, headers: dict[str, Any] | None = None) -> None:
        super().__init__(
            status_code=404,
            detail='Spy Cat not found',
            headers=headers
        )


class ValidateBreedError(HTTPException):
    def __init__(self, headers: dict[str, Any] | None = None) -> None:
        super().__init__(
            status_code=400,
            detail='Invalid breed',
            headers=headers
        )