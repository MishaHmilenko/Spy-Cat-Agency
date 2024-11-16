from typing import Any

from fastapi import HTTPException


class TargetNotExist(HTTPException):
    def __init__(self, headers: dict[str, Any] | None = None) -> None:
        super().__init__(
            status_code=404,
            detail='Target not found',
            headers=headers
        )


class TargetAlreadyComplete(HTTPException):
    def __init__(self, headers: dict[str, Any] | None = None) -> None:
        super().__init__(
            status_code=409,
            detail='Target already complete',
            headers=headers
        )


class TargetNotBelongsToMission(HTTPException):
    def __init__(self, headers: dict[str, Any] | None = None) -> None:
        super().__init__(
            status_code=404,
            detail='Target not belongs to this mission',
            headers=headers
        )
