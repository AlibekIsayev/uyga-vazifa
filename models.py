from tokenize import String

from sqlalchemy import Column, Integer

from database import Base

class User (Base) :


    tablename= "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String, unique=True)  #takrorlanmagan email
    password = Column(String)


class Books (Base) :
    __tablename__="kitoblar"

    id = Column(Integer , primary_key=True , index=True)
    name = Column(String , unique=True)
    count = Column(Integer)
    price = Column(Integer)