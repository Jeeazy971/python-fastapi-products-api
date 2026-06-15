from sqlalchemy.orm import Mapped, mapped_column

from app.database.session import Base


class Goal(Base):
    __tablename__ = "goals"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    category: Mapped[str] = mapped_column()
    is_completed: Mapped[bool] = mapped_column(default=False)
