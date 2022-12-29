import sys
import pprint
import additional_inf
import orm

def comndErr():
	print("You have to enter the command from 1 to 5 ERROR")


def comand_identification():
	return input('Enter command : ')

def table_name():
	print('Your table_name name: train, ticket, railcar ')
	return input('Enter table_name name ')

def print_info(my_dict):
    pprint.pprint(my_dict)

def input_colums_str_upd():
    return input("Enter column which you want to update separated by'|':")

def input_colums_str_search():
    return input("Enter column where you want to search values separated by'|':")

def input_inf_for_column(column_name):
    return input(column_name + ':')

def input_inf_for_table(attr_class):
    values = []
    for attr in attr_class:
        values.append(input_inf_for_column(attr))
    return values

def finding_fields_which_you_want_change():
    return input("Enter column atribute,based on which you want to change this fileld like 'Column_name = 'value'' and press Enter,when you want to stop enter columns press '-' and press Enter:")

def Data():
    return input('Enter value: ')

def row():
    return int(input('Enter value: '))

def tablevalid():
    print('The table_name name is wrong ERROR')
    sys.exit()

def choose_scenario_search():
    scenario = input("Choose presearch scenario which you want:")
    return (int(scenario) - 1)

def menu():
    print('Update press 1')
    print('Add press 2')
    print('Delete press 3')
    print('Random press 4')
    print('Search press 5')
    print('Info about tables press 6')
    print('If you want take out from app press "-"')
    print('Please print all not numeric types like int and float,like this "value"')


def take_inf_based():
    field_value = {}
    while (1):
        temp_str = finding_fields_which_you_want_change()
        if(temp_str == "-"):
            break
        field, value = temp_str.split('=')
        field_value.update({field: value})

    return field_value

def take_inf_for_adding(table_name):
    attrs_class = orm.get_attr_name_of_class(table_name)
    field_value = dict(zip(attrs_class, input_inf_for_table(attrs_class)))
    return field_value

def take_inf_about_param(str_of_columns, ):
    columns = str_of_columns.split("|")
    dict_of_updating_column = {}
    for column in columns:
        dict_of_updating_column.update({column: input_inf_for_column(column)})
    return dict_of_updating_column

def take_searching_rows(str_of_columns):
    columns = str_of_columns.split("|")
    dict_of_tacking = {}
    for column in columns:
        type_ = search_type_of_column(column)
        match type_:
                case "int":
                    dict_of_tacking[column] = input(f"please input range int numbers for {column} separated by '|'").split("|")
                case "str":
                    dict_of_tacking[column] = input(f"please input scenario for {column} str")
                case "time":
                    dict_of_tacking[column] = input(f"please input range between two dates for {column} separated by '|'").split("|")
    return dict_of_tacking


def search_type_of_column(column_name):
    for tables in additional_inf.parametrs:
        for parametr in additional_inf.parametrs[tables]:
            if(column_name == parametr[0]):
                return parametr[1]
    raise("this column is not exist")

def print_searching_values(list_of_searching):
    print(list_of_searching)
