from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas, auth

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = auth.hash_password(user.password)
    new_user = models.User(username=user.username, password=hashed)
    db.add(new_user)
    db.commit()
    return {"message": "User created"}

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_token({"user_id": db_user.id})
    return {"access_token": token}

@router.post("/tasks")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(title=task.title, owner_id=1)
    db.add(new_task)
    db.commit()
    return {"message": "Task created"}

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()
