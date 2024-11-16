from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import Base


class Mission(Base):
    __tablename__ = "mission"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)

    executor_id: Mapped[int] = mapped_column(ForeignKey('spy_cat.id'), nullable=True)

    executor: Mapped['SpyCat'] = relationship(back_populates='missions', uselist=False)
    targets: Mapped[list['Target']] = relationship(back_populates='missions', lazy='dynamic')

