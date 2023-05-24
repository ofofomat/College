import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect('banco.db')
        self.createTables()

    def createTables(self):
        try:
            c = self.connection.cursor()

            c.execute("""create table if not exists employees (
                                 id_employee integer primary key autoincrement,
                                 name text not null,
                                 gender text,
                                 birth_date text,
                                 qnt_dependent integer,
                                 role text,
                                 wage integer,
                                 id_department integer)""")
            self.connection.commit()
            print("Database ok")
            c.close()

        except sqlite3.Error as error:
            print("Error trying to connect into SQLite", error)
