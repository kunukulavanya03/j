from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base, User, Item
from schemas import UserCreate, UserResponse, ItemCreate, ItemResponse
import logging

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Backend_Api_For_J,_A_React-Based_Frontend_Application._The_Api_Will_Provide_Data_Storage,_Retrieval,_And_Manipulation_Capabilities_For_The_Frontend_Application. API",
    description="Complete backend API",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Backend_Api_For_J,_A_React-Based_Frontend_Application._The_Api_Will_Provide_Data_Storage,_Retrieval,_And_Manipulation_Capabilities_For_The_Frontend_Application. API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "backend_api_for_j,_a_react-based_frontend_application._the_api_will_provide_data_storage,_retrieval,_and_manipulation_capabilities_for_the_frontend_application."}

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=list[ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(Item).offset(skip).limit(limit).all()
    return items

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)