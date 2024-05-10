from sqlalchemy import Column, String, Boolean, DateTime
from database import Base
from datetime import datetime
from database import engine

class FeatureToggle(Base):
    __tablename__ = "feature_toggles"

    name = Column(String, primary_key=True, index=True)
    description = Column(String)
    state = Column(Boolean, default=False)
    environment = Column(String, nullable=True)
    owner = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)


Base.metadata.create_all(bind=engine)