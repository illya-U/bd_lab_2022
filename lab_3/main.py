import psycopg2
from psycopg2 import errors
from model import *
from view import *
import sys


def request():
    while(1):
        menu()
        input_command = comand_identification()

        if (input_command == '1'):
            table = table_name()
            str_of_columns = input_colums_str_upd()
            field_value = take_inf_about_param(str_of_columns)
            based_field_value = take_inf_based()
            db.updt(table, field_value, based_field_value)
        elif (input_command == '2'):
            table = table_name()
            field_value = take_inf_for_adding(table)
            db.add_inf(table, field_value)
        elif (input_command == '3'):
            table = table_name()
            based_field_value = take_inf_based()
            db.delete(table, based_field_value)
        elif (input_command == '4'):
            table = table_name()
            data = Data()
            db.random(table, data)
        elif (input_command == '5'):
            pass
            # scenario = choose_scenario_search()
            # str_of_columns = input_colums_str_search()
            # dict_of_searching_var = take_searching_rows(str_of_columns)
            # list_of_searching = search(con, cursor_r, scenario, dict_of_searching_var)
            # print_searching_values(list_of_searching)
        elif (input_command == '-'):
            break
        elif (input_command is not str(range(5))):
            comndErr()

    sys.exit()

db = DB()
request()