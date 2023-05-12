from flask import Flask, request, jsonify

app = Flask(__name__)

# list for materials
materials = ['banana', 'apple', 'passion fruit']
# list for quantities of materials
quantities = [10, 2, 278]


@app.route('/', methods=['GET'])
def say_hello():
    return "<h1>Hello mate, Server's up!</h1>"


@app.route('/materials', methods=['GET'])
def get_materials():
    items = []
    for i in range(len(materials)):
        result = {
            'material': {
                'id': i,
                'name': materials[i],
                'quantity': quantities[i]
            }
        }
        items.append(result)
    response = items, 200
    return response


@app.route('/materials', methods=['POST'])
def add_materials():
    request_data = request.get_json()
    materials.append(
        request_data['material']['name']
    )
    quantities.append(
        request_data['material']['qtde']
    )
    return 'Successfully created', 201


@app.route('/materials/<int:id>', methods=['GET'])
def get_a_material(id):
    item = {
        'material': {
            'id': id,
            'name': materials[id],
            'qtde': quantities[id]
        }
    }
    response = item, 200
    return response


@app.route('/materials/<int:id>', methods=['PUT'])
def alter_a_material(id):
    request_data = request.get_json()
    materials.pop(id)
    quantities.pop(id)
    materials.insert(id,
                     request_data['material']['name']
                     )
    quantities.insert(id,
                      request_data['material']['qtde']
                      )
    return 'Successfully changed', 200


@app.route('/materials/<int:id>', methods=['DELETE'])
def delete_a_material(id):
    materials.pop(id)
    quantities.pop(id)
    items = []
    for i in range(len(materials)):
        result = {
            'material': {
                'id': i,
                'name': materials[i],
                'quantity': quantities[i]
            }
        }
        items.append(result)
    response = items, 200
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='5000')
