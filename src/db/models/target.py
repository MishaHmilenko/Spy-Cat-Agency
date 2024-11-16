from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import Base


class Target(Base):
    __tablename__ = "target"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    country: Mapped[str] = mapped_column(String(50), nullable=False)
    notes: Mapped[str] = mapped_column(String(255), nullable=True)
    complete: Mapped[bool] = mapped_column(nullable=False, default=False)

    mission_id: Mapped[int] = mapped_column(ForeignKey('mission.id'), nullable=True)

    missions: Mapped["Mission"] = relationship(back_populates='targets')
