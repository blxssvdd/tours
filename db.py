from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column


engine = create_engine("sqlite:///tours.db")
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def create_db():
    Base.metadata.create_all(bind=engine)


class Tour(Base):
    __tablename__ = "tours"

    id: Mapped[int] = mapped_column(primary_key=True)
    country: Mapped[str] = mapped_column(String(100))
    price: Mapped[str] = mapped_column(String())