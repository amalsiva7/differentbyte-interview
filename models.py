from sqlalchemy.orm import mapped_column, Mapped
from uuid import uuid4, UUID as PyUUID
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class Contact(Base):
    __tablename__ = "contact"

    id: Mapped[PyUUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, index=True)
    message: Mapped[str | None] = mapped_column(nullable=True)
