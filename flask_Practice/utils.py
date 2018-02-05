import  os, json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
BASE = declarative_base()
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"config.json")) as fp:
     config = json.loads(fp.read())

ENGINE = create_engine(config["dbconnector"]+"://"+config["username"]+":"+
                    config["password"]+"@"+config["host"]+"/"+config["dbname"])

Session = sessionmaker()
Session.configure(bind=ENGINE)
session = Session()



