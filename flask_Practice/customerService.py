import os, sys, json, ast
from utils import session
from flaskModel import Customer,Bill

class customer_Services:

    def insert_customer(self,local_data):
        try:
            cust_name = local_data['cust_name']
            cust_address = local_data['cust_address']
            customer = Customer(cust_name=cust_name,cust_address=cust_address)
            session.add(customer)
            session.commit()
            print "success"
            return "Success"
        except Exception as e:
            print e,"Customer  insert"
            return "Error"

    def get_contact_id_by_name(cust_name):
        try:
            contact_details = session.query(Customer). \
                filter(Customer.cust_name == cust_name).all()
            return contact_details[0].contact_id
        except Exception as e:
            print e, "Exception in get cust_id"
            return None

    # # def get_contact_name_by_id(data_id):
    #     try:
    #         contact_details = session.query(Contacts). \
    #             filter(Contacts.contact_id == data_id).all()
    #         return contact_details[0].contact_name
    #     except Exception as e:
    #         print e, "Exception in get event_id"
    #         return None

    def fetch_data(self,data_name):
        try:
            customer = session.query(Customer).filter(Customer.cust_name ==
                                                        data_name).one()
            cust_details = {
                                "cust_id":customer.cust_id,
                                "cust_name":customer.cust_name,
                               "cust_address":customer.cust_address,

                               }
            return cust_details
        except Exception as e:
            print e, "Exception in fetch_cust"
            return "Error"


    def fetch_records(self):
        try:
            cust_data = list()
            cust_details = session.query(Customer).all()
            for cust in cust_details:
                cust_data.append(self.fetch_data(cust.cust_name))
            return cust_data
        except Exception as e:
            print e, "Exception fetch_cust_records"
            return "Error"

    def delete_data(self,data_name):
        print type(data_name)
        try:
            cust = session.query(Customer).filter(Customer.cust_name == data_name).first()
            bill = session.query(Bill).filter(Bill.cust_id == cust.cust_id)
            print cust
            print data_name
            session.delete(cust)
            session.delete(bill)
            session.commit()
            return "Success"
        except Exception as e:
            print e, "Exception in delete Customer"
            return "Error"

