from flask import Flask, request, jsonify
from employee import Employee

app = Flask(__name__)


@app.route('/', methods=['GET'])
def landing_page():
    return f'<h1>API is working!</h1>'


@app.post('/employees')
def post_employee():
    employee_data = request.get_json()
    new_employee = Employee(employee_data['role'], employee_data['id_department'], employee_data['qnt_dependent'],
                            employee_data['name'], employee_data['gender'], employee_data['birth_date'], employee_data['wage'])
    new_employee.set_name(employee_data['name'])
    response = new_employee.insert_employee()
    return f"{response}", 200


@app.get('/employees')
def get_employees():
    labor = []
    for i in range(21):
        emp = Employee("", 0, 0, "", "", "", 0)
        emp.select_employee(str(i))
        if emp.id_employee == None:
            pass
        else:
            response = {
                "id_employee": emp.id_employee,
                "role": emp.role,
                "id_department": emp.id_department,
                "qnt_dependent": emp.qnt_dependent,
                "name": emp.get_name(),
                "gender": emp.get_gender(),
                "birth_date": emp.get_birth_date(),
                "wage": emp.wage
            }
            labor.append(response)
    return jsonify({"employees": labor})


@app.get('/employees/<string:id>')
def get_employee(id):
    emp = Employee("", 0, 0, "", "", "", 0)
    emp.select_employee(id)
    response = {
        "role": emp.role,
        "id_department": emp.id_department,
        "qnt_dependent": emp.qnt_dependent,
        "name": emp.get_name(),
        "gender": emp.get_gender(),
        "birth_date": emp.get_birth_date(),
        "wage": emp.wage
    }
    if emp.id_employee == None:
        return f"There's no employee n.{id}"
    else:
        print(f"Employee n.{id} was found")
        return jsonify({'employee': response})


@app.put('/employees/<string:id>')
def alter_employee(id):
    employee_data = request.get_json()
    emp = Employee("", 0, 0, "", "", "", 0)
    emp.select_employee(id)
    if emp.id_employee == None:
        return f"There's no employee n.{id}"
    else:
        emp.update_employee(employee_data)
        return f"Employee n.{id} updated successfully!", 200


@app.delete('/employees/<string:id>')
def delete_employee(id):
    emp = Employee("", 0, 0, "", "", "", 0)
    emp.select_employee(id)
    if emp.id_employee == None:
        return f"There's no employee n.{id}"
    else:
        return f"{emp.delete_employee()}"


if __name__ == '__main__':

    app.run(host="0.0.0.0", port="5000", debug=True)
