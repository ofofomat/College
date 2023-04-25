from flask import Flask, request, jsonify
import json
import uuid

app = Flask(__name__)

# Customers list
customers = []


@app.route('/', methods=['GET'])
def landing_page():
    return "<h1>Welcome to your Flask API</h1>"


@app.route('/customers', methods=['GET'])
def get_customers():
    response = jsonify({'customers': customers}), 200
    return response


@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    response = jsonify({'customer': customers[customer_id]}), 200
    return response


@app.route('/customers/<int:customer_id>', methods=['PUT'])
def alter_customer(customer_id):
    request_data = request.get_json()
    customer_data = request_data['customer']
    idCustomer = customers[customer_id]['id']
    customer_data
    customers.pop(customer_id)
    customers.insert(customer_id, {
        'id': idCustomer,
        'name': customer_data['name'],
        'email': customer_data['email']
    })
    return 'Altered', 200


@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customers.pop(customer_id)
    return 'OK', 204


@app.route('/customers', methods=['POST'])
def new_customer():
    request_data = request.get_json()
    customer_data = request_data['customer']

    customers.append(
        {'id': uuid.uuid4(),
         'name': customer_data['name'],
         'email': customer_data['email']})
    return 'OK', 201


if __name__ == '__main__':

    app.run(host="0.0.0.0", port="5000", debug=True)
