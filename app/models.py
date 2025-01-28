from datetime import datetime, timezone
from sqlalchemy import Column, Integer, Sequence, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database import Base

class Player(Base):
    __tablename__ = "mlb_players"
    id = Column(Integer, primary_key=True)
    fullName = Column(String,  nullable=False)

