import psycopg2
import sqlalchemy

import additional_inf
import base
from sqlalchemy import *
import orm



class DB:
    def __init__(self):

        self.session = base.Session()
        self.con = psycopg2.connect(
                    database="railway ticket sales service",
                    user="postgres",
                    password="1111",
                    host="localhost",
                    port="5432"
                )
        self.con.set_session(autocommit=True)
        self.curso_r = self.con.cursor()

    def random(self, table_name, n):

        field_type = {additional_inf.parametrs[table_name][1:]}

        try:
            for i in range(int(n)):
                self.add_inf(table_name, {field: additional_inf.randomvalue_type[type] for field, type in field_type})
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as err:
            print(err)
            self.session.rollback()
            print(f'WARNING:Error {err}')

    def delete(self, table_name, field_value):
        try:
            table_class = orm.get_class_by_tablename(table_name)

            filter_txt = dict_to_sql_str(field_value)

            self.session.query(table_class).filter(text(filter_txt)).delete(synchronize_session=False)
            self.session.commit()
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as err:
            print(err)
            self.session.rollback()
            print(f'WARNING:Error {err}')

    def add_inf(self, table_name, field_value):
        try:
            obj = orm.get_class_by_tablename(table_name)(**field_value)
            self.session.add(obj)
            self.session.commit()
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as err:
            print(err)
            self.session.rollback()
            print(f'WARNING:Error {err}')

    def updt(self, table_name, field_value, based_field_value):
        try:
            table_class = orm.get_class_by_tablename(table_name)

            filter_txt = dict_to_sql_str(based_field_value)

            self.session.query(table_class).filter(text(filter_txt)).update(field_value, synchronize_session=False)

            self.session.commit()

        except (Exception, sqlalchemy.exc.SQLAlchemyError) as err:
            print(err)
            self.session.rollback()
            print(f'WARNING:Error {err}')


    def search(self, column_name, *tabels):
        try:
            if self.check_for_present(self.session, column_name, *tabels):
                for el in tabels:
                    print("Please input filter type for each column: ")
                    filter = input()
                    if filter.lower() == 'between':
                        print("Please input column name and first and second limits")
                        self.search_between(self.session, el, input(), input(), input())
                    elif filter.lower() == 'is null':
                        print("Please input column name")
                        self.search_is_null(self.session, el, input())
                    elif filter.lower() == 'easy':
                        print("Please input column name and value")
                        self.search_easy(self.session, el, input(), input())
                    else:
                        print("Missing option")
        except(Exception, self.session) as error:
            print(error)
            return False

    @staticmethod
    def get_column_type(con, table, column):
        try:
            cur = con.cursor()
            cur.execute("""SELECT column_name, data_type FROM information_schema.columns
                   WHERE table_name = '{}'""""".format(table))
            for table in cur.fetchall():
                if column in table: return table[1]
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def auto_gen_int(con, rows_number):
        try:
            cur = con.cursor()
            cur.execute("SELECT num "
                        "FROM GENERATE_SERIES(1, {}) AS s(num) "
                        "ORDER BY RANDOM() "
                        "LIMIT {}".format(rows_number, rows_number))
            return cur.fetchall()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def column_data(con, table_name, column_name):
        try:
            cur = con.cursor()
            cur.execute('SELECT {} FROM public."{}"'.format(column_name, table_name))
            values = []
            for val in cur.fetchall():
                values.append(*val)
            return values
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def get_input_format(con, table_name):

        columns = orm.get_class_by_tablename(table_name).table.columns.keys()
        print(columns)
        return columns

    @staticmethod
    def check_for_present(con, column_name, *tabels):
        for el in tabels:
            val_list = []
            print(el)
            columns = con.get_input_format(con, el)
            if column_name not in columns:
                print('{} is not in {} table'.format(column_name, el))
                return False
        return True

    @staticmethod
    def search_between(con, table_name, column_name, limit1, limit2):
        try:
            table_class = orm.get_class_by_tablename(table_name)
            filter_txt = '{} BETWEEN {} AND {}'.format(column_name, limit1, limit2)
            query = con.query(table_class).filter(text(filter_txt))
            print(*query.all())
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as error:
            print(error)

    @staticmethod
    def search_is_null(con, table_name, column_name):
        try:
            table_class = orm.get_class_by_tablename(table_name)
            filter_txt = '{} IS NULL'.format(column_name)
            query = con.query(table_class).filter(text(filter_txt))
            print(*query.all())
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as error:
            print(error)

    @staticmethod
    def search_easy(con, table_name, column_name, value):
        try:
            table_class = orm.get_class_by_tablename(table_name)
            col_name = table_class.dict[column_name]
            filter_txt = '{} = {}'.format(column_name, value)
            query = con.query(table_class).filter(text(filter_txt)).order_by(col_name)
            print(*query.all())
        except (Exception, sqlalchemy.exc.SQLAlchemyError) as error:
            print(error)



    def __del__(self):
        pass
        # self.session.close()
        # self.curso_r.close()
        # self.con.close()


def dict_to_sql_str(field_value):
    mass_of_filter_str = list(map(lambda key, value: "{} = '{}'".format(key, value), field_value.items()))

    return ' AND '.join(mass_of_filter_str)






