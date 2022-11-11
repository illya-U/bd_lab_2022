import psycopg2
from psycopg2 import errors
from model import *
from view import *
import sys


def request():
    input_command = comand_identification()

    if (input_command == '1'):
        table = table_name()
        str_of_columns = input_colums_str_upd()
        str_of_updating_column= take_inf_about_param(str_of_columns)
        str_of_based_column = take_inf_based()
        updt(table,str_of_updating_column,str_of_based_column)
    elif (input_command == '2'):
        table = table_name()
        inf = take_inf_for_adding(table)
        add_inf(table,inf)
    elif (input_command == '3'):
        table = table_name()
        str_of_based_column = take_inf_based()
        delete(table,str_of_based_column)
    elif (input_command == '4'):
        table = table_name()
        data = Data()
        random(table, data)
    elif (input_command == '5'):
        scenario = choose_scenario_search()
        str_of_columns = input_colums_str_search()
        dict_of_searching_var = take_searching_rows(str_of_columns)
        list_of_searching = Search(scenario,dict_of_searching_var)
        print_searching_values(list_of_searching)
    elif (input_command == '6'):
        print_info(info())
    elif (input_command is not str(range(6))):
        comndErr()
        sys.exit()


menu()

request()