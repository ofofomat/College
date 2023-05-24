import datetime


class Person:
    # __renda = None
    __name = None
    __gender = None
    __birth_date = None

    # Construtor / Visbilidade (atributos publicos)
    def __init__(self, name,  gender, birth_date):
        self.set_name(name)
        self.set_gender(gender)
        self.set_birth_date(birth_date)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def get_birth_date(self):
        return self.__birth_date

    def get_age(self):
        age = int(datetime.datetime.now().year) - \
            int(datetime.date.replace(self.birth_date).year)
        return age

    def set_income(self, value):
        self.__income = value

    def get_income(self):
        return self.__income
