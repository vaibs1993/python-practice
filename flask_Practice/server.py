import json
from flask import Flask, request, abort, jsonify
from customerService import customer_Services as cust
from billService import bill_Service as bill

app = Flask(__name__)
c = cust()
b = bill()
#add new Customer
@app.route('/customers', methods = ['POST'])
def add_customer():
    try:
        local_data = request.json
        print local_data
        c.insert_customer((local_data))
        return "Added Customer SuccessFully"
    except Exception as error:
        print error
        print "ERROR"

#get all customer
@app.route('/customer')
def get_all_customer():
    cust_name = request.args.get("cust")
    print cust_name
    if cust_name is None:
        try:
            data = c.fetch_records()
            print data
            return str(json.dumps(c.fetch_records()))
        except Exception as error:
            print error
    else:
        try:
            print "in else"
            data = c.fetch_data(cust_name)
            print data
            return json.dumps(data)
        except Exception as e:
            print e
            return "Error"


@app.route('/customer', methods = ['POST'])
def get_customer():
    try:
        data = request.json
        print data.name
        return str(json.dumps(c.fetch_data(data.name)))
    except Exception as error:
        print error


@app.route('/customer', methods = ['delete'])
def delete_customer():
    try:
        data = request.json
        print data["cust_name"]
        c.delete_data(data["cust_name"])
        print "Deleted Sucessfully"
        return "Succes"
    except Exception as error:
        print error
        return "Error"


##################Bill###########

#add new Bill
@app.route('/bill', methods = ['POST'])
def add_bill():
    try:
        local_data = request.json
        print local_data
        b.insert_bill((local_data))
        return "Added Bill SuccessFully"
    except Exception as error:
        print error
        print "ERROR"

#get all customer
@app.route('/bill')
def get_all_bill():
    bill_id = request.args.get("bill_id")
    print bill_id
    if bill_id is None:
        try:
            data = b.fetch_records()
            print data
            return str(json.dumps(b.fetch_records()))
        except Exception as error:
            print error
    else:
        try:
            print "in else"
            data = b.fetch_data(bill_id)
            return json.dumps(data)
        except Exception as e:
            print e
            return "Error"



@app.route('/bill', methods = ['delete'])
def delete_bill():
    try:
        data = request.json
        print data["bill_id"]
        c.delete_data(data["bill_id"])
        print "Deleted Sucessfully"
        return "Succes"
    except Exception as error:
        print error
        return "Error"



if __name__ == '__main__':
    print "starting moncontrol serever at port 8000"
    app.run('0.0.0.0',port=8000)
