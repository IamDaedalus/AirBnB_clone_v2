#!/usr/bin/python3

import os
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base

__engine = None
__session = None

def __init(self):

    db = os.environ['HBNB_TYPE_STORAGE']
    user = os.environ['HBNB_MYSQL_USER']
    passwd = os.environ['HBNB_MYSQ_LPWD']

    db_url = f"mysql+mysqldb://{user}:{passwd}@localhost/{db}"

    self.__engine = create_engine(db_url, pool_pre_ping=True)
    if os.environ['HBNB_ENV'] == "test":
        Base.metadata.drop_all(self.__engine)
