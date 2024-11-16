from typing import Any

from fastapi import HTTPException


class MissionAlreadyAssignedError(HTTPException):
    def __init__(self, headers: dict[str, Any] | None = None) -> None:
        super().__init__(
            status_code=409,
            detail='Mission already assigned',
            headers=headers
        )


class MissionNotExist(HTTPException):
    def __init__(self, headers: dict[str, Any] | None = None) -> None:
        super().__init__(
            status_code=404,
            detail='Mission not found',
            headers=headers
        )
