from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import schemas, models
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/feature-toggles/", response_model=schemas.Toggle)
def create_feature_toggle(toggle: schemas.ToggleCreate, db: Session = Depends(get_db)):
    existing_toggle = db.query(models.FeatureToggle).filter(models.FeatureToggle.name == toggle.name).first()
    if existing_toggle:
        raise HTTPException(status_code=409, detail="Toggle with this name already exists")
    db_toggle = models.FeatureToggle(**toggle.dict())
    db.add(db_toggle)
    db.commit()
    db.refresh(db_toggle)
    return db_toggle

@router.get("/feature-toggles/", response_model=List[schemas.Toggle])
def get_all_feature_toggles(db: Session = Depends(get_db)):
    return db.query(models.FeatureToggle).all()

@router.get("/feature-toggles/{toggle_name}", response_model=schemas.Toggle)
def get_feature_toggle(toggle_name: str, db: Session = Depends(get_db)):
    toggle = db.query(models.FeatureToggle).filter(models.FeatureToggle.name == toggle_name).first()
    if toggle is None:
        raise HTTPException(status_code=404, detail="Toggle not found")
    return toggle

@router.put("/feature-toggles/{toggle_name}", response_model=schemas.Toggle)
def update_feature_toggle(toggle_name: str, toggle: schemas.ToggleUpdate, db: Session = Depends(get_db)):
    db_toggle = db.query(models.FeatureToggle).filter(models.FeatureToggle.name == toggle_name).first()
    if db_toggle is None:
        raise HTTPException(status_code=404, detail="Toggle not found")
    for field, value in toggle.dict().items():
        setattr(db_toggle, field, value)
    db.commit()
    db.refresh(db_toggle)
    return db_toggle
