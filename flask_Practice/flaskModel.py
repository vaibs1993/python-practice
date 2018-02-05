import os, sys
from utils import BASE, ENGINE
from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import *

class Customer(BASE):
    __tablename__ = "Customer"
    cust_id = Column(INTEGER, primary_key=True)
    cust_name = Column(String(20))
    cust_address = Column(String(100))

class Bill(BASE):
    __tablename__ = "Bill"
    bill_id = Column(INTEGER,primary_key=True)
    cust_id = Column(INTEGER, ForeignKey("Customer.cust_id"))
    bill_amount = Column(INTEGER)



BASE.metadata.create_all(ENGINE)

