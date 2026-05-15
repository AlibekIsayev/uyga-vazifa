from http.client import HTTPException

import uvicorn
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


# update
@app.put("/updateuser/{user_id}")
def updateuser(user_id: int ,update_data : UserSchemas, db : Session = Depends (get_db)):
    # id bo'yicha userlarni topish
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException()

    user.fullname = update_data.fullname
    user.email = update_data.email

    # db ga saglash
    db.commit()
    db.refresh(user)

    return {"Message ": " User updated", " User -- >": user}


#delete

@app.delete("/deleteuser/{user_id}")
def deleteuser(user_id: int , db : Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404 , detail=" user topilmadi")


    db.delete(user)
    db.commit()
    return {"Message " : "Deleted" }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# if __name__ == '__main__':

