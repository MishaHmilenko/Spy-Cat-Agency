from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import Base


class SpyCat(Base):
    __tablename__ = "spy_cat"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    years_of_experience: Mapped[int] = mapped_column(nullable=False)
    breed: Mapped[str] = mapped_column(String(30), nullable=False)
    salary: Mapped[float] = mapped_column(nullable=False)

    missions: Mapped["Mission"] = relationship(back_populates='executor')