from sqlalchemy import Column, Integer, String, Text
from database import Base

class LegalDocument(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    keywords = Column(Text, nullable=True)
    entities = Column(Text, nullable=True)
