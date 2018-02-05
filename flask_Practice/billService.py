import os, sys, json, ast
from utils import session
from flaskModel import Bill, Customer
#from customerService import customer_Service


class bill_Service:
    def insert_bill(self, local_data):
        try:
            cust_id = local_data['cust_id']
            bill_amount = local_data['bill_amount']
            bill = Bill(cust_id=cust_id,bill_amount=bill_amount)
            session.add(bill)
            session.commit()
            return "Success"
        except Exception as e:
            print e,"Bill insert"
            return "Error"


    def fetch_data(self, data_name):
        try:
            bill = session.query(Bill).filter(Bill.bill_id ==
                                                        data_name).one()
            customer = session.query(Customer).filter(Customer.cust_id ==bill.cust_id).one()
            cust_details = {
                                "cust_id":bill.cust_id,
                                "cust_name":customer.cust_name,
                               "cust_address":customer.cust_address,
                                "bill_amount":bill.bill_amount
                         }
            return cust_details
        except Exception as e:
            print e, "Exception in fetch_bill"
            return "Error"


    def fetch_records(self):
        try:
            bill_data = list()
            bill_details = session.query(Bill).all()
            for bill in bill_details:
                bill_data.append(self.fetch_data(bill.bill_id))
            return bill_data
        except Exception as e:
            print e, "Exception fetch_cust_records"
            return "Error"

    def delete_data(data_name):
        try:
            bill = session.query(Bill).filter(Bill.bill_id == data_name).first()
            session.delete(bill)
            session.commit()
            return "Success"
        except Exception as e:
            print e, "Exception in delete Bill"
            return "Error"

