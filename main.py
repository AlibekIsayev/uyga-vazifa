from fastapi import FastAPI
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal
from models import User

app = FastAPI()


class UserSchemas(BaseModel):
    fullname: str
    email: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/createuser")

def createuser(user_data: UserSchemas, db: Session = Depends(get_db)):
    newuser = User(fullname=user_data.fullname, email=user_data.email)
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return {"Message: ": "Saqlamndi", "user-->": newuser}



@app.get("getalluser")
def getalluser(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users







# if __name__ == '__main__':

