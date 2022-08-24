from email.policy import default
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Blogs(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    published = Column(Boolean, default=False)