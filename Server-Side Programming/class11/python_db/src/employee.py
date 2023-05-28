import sqlite3
from person import Person
from database import Database


class Employee(Person):  # Herança

    def __init__(self, role, id_department, qnt_dependent, name, gender, birth_date, wage):
        super().__init__(name, gender, birth_date)
        self.id_employee = None
        self.role = role
        self.id_department = int(id_department)
        self.wage = int(wage)
        self.qnt_dependent = int(qnt_dependent)
        self.database = Database()

    @property
    def id_employee(self):
        return self._id_employee

    @id_employee.setter
    def id_employee(self, id_employee):
        self._id_employee = id_employee

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    @property
    def id_department(self):
        return self._id_department

    @id_department.setter
    def id_department(self, id_department):
        self._id_department = id_department

    @property
    def wage(self):
        return self._wage

    @wage.setter
    def wage(self, wage):
        self._wage = wage

    @property
    def qnt_dependent(self):
        return self._qnt_dependent

    @qnt_dependent.setter
    def qnt_dependent(self, qnt_dependent):
        self._qnt_dependent = qnt_dependent

    def calc_wage(self, extra_hours):
        eh_value = (self.wage / 30) / 8
        total_wage = (extra_hours * eh_value) + self.wage
        self.set_income(total_wage)
        return total_wage

    def set_income(self, valor):  # Polimorfismo
        if self.qnt_dependent > 0:
            bonus = self.qnt_dependent * 80
            self.income = bonus + valor
        else:
            pass

    def insert_employee(self):
        try:

            c = self.database.connection.cursor()

            c.execute("insert into employees (name, gender, birth_date, qnt_dependent, role, wage, id_department) values('" + self.get_name() + "', '" + self.get_gender() +
                      "', '" + self.get_birth_date() + "', '" + str(self.qnt_dependent) + "', '" + self.role + "', '" + str(self.wage) + "', '" + str(self.id_department) + "')")
            id_generated = c.lastrowid

            self.database.connection.commit()
            c.close()
            return True, id_generated, "Employee successfully registered!"
        except sqlite3.Error as er:
            return False, 0, "There's been an error while registering the employee"

    def update_employee(self, data: dict):
        try:

            c = self.database.connection.cursor()

            c.execute("update employees set name = '" + data['name'] + "', gender = '" + data['gender'] + "', birth_date = '" + data['birth_date'] + "', qnt_dependent = '" + data['qnt_dependent'] +
                      "', role = '" + data['role'] + "', wage = '" + data['wage'] + "', id_department = '" + data['id_department'] + "' where id_employee = " + str(self.id_employee) + " ")

            self.database.connection.commit()
            c.close()

            return True, "Employee register updated successfully!"
        except sqlite3.Error as er:
            return False, "There's been an error while updating the employee"

    def delete_employee(self):
        try:

            c = self.database.connection.cursor()

            c.execute("delete from employees where id_employee = " +
                      str(self.id_employee) + " ")

            self.database.connection.commit()
            c.close()

            return True, "Employee deleted successfully!"
        except sqlite3.Error as er:
            return False, "There's been an error while deleting the employee"

    def select_employee(self, id_employee: str):
        try:

            c = self.database.connection.cursor()
            c.execute(
                "select * from employees where id_employee = " + id_employee + "  ")

            line = c.fetchone()

            if line is None:
                return False, "Employee not found"

            self.id_employee = line[0]
            self.set_name(line[1])
            self.set_gender(line[2])
            self.set_birth_date(line[3])
            self.qnt_dependent = int(line[4])
            self.role = line[5]
            self.wage = int(line[6])
            self.id_department = int(line[7])

            c.close()

            return True, "Search was successfully done!"
        except sqlite3.Error as er:
            return False, "There's been an error while searching the employee"
