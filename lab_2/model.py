import psycopg2
import additional_inf


def setup_conf(func):
    def wrapper(*args, **kwargs):
        con = psycopg2.connect(
            database="railway ticket sales service",
            user="postgres",
            password="1111",
            host="localhost",
            port="5432"
        )
        con.set_session(autocommit=True)
        curso_r = con.cursor()
        smth = func(con, curso_r, *args, **kwargs)
        curso_r.close()
        con.close()
        return smth
    return wrapper


@setup_conf
def info(con, cursor_r):
    dict_of_all_tables = {}
    try:
        for table in additional_inf.parametrs:
            dict_of_all_tables[table] = []
            flag_of_take_memory = 1
            for param in additional_inf.parametrs[table]:
                param = param[0]
                cursor_r.execute(additional_inf.set_command["inf"].replace("table", table).replace("param", param))
                list_of_all_parametrs = cursor_r.fetchall()
                if (flag_of_take_memory):
                    for memory_take in range(len(list_of_all_parametrs)):
                        dict_of_all_tables[table].append({})
                    flag_of_take_memory = 0
                for i in range(len(list_of_all_parametrs)):
                    dict_of_all_tables[table][i][param] = list_of_all_parametrs[i][0]
            flag_of_take_memory = 1
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')
    else:
        return dict_of_all_tables

@setup_conf
def random(con, cursor_r, table_name, n):
    param = ",".join([*map(lambda x:additional_inf.parametrs[table_name][x][0], range(1, len(additional_inf.parametrs[table_name])))])
    try:
        for i in range(int(n)):
            take_sql_str_to_two_stream(cursor_r, additional_inf.set_command["random"][table_name].replace("parametrs", param))
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')

@setup_conf
def delete(con, cursor_r, table_name, str_of_based_column):
    try:
        take_sql_str_to_two_stream(cursor_r, additional_inf.set_command["delete"].replace("str_of_based_column", str_of_based_column).replace("table_name", table_name))
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')

@setup_conf
def add_inf(con, cursor_r, table_name, mass):
    param = ",".join([*map(lambda x: additional_inf.parametrs[table_name][x][0], range(1, len(additional_inf.parametrs[table_name])))])
    mass = [*map(lambda x: "'{0}'".format(x), mass)]
    values = ",".join(mass)
    try:
        take_sql_str_to_two_stream(cursor_r, additional_inf.set_command["add_inf"].replace("table_name", table_name).replace("parametrs", param).replace("values", values))
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')


@setup_conf
def updt(con, cursor_r, table_name, str_of_updating_column, str_of_based_column):
    try:
        take_sql_str_to_two_stream(cursor_r, additional_inf.set_command["upd_inf"].replace("table_name", table_name).replace("str_of_updating_column", str_of_updating_column).replace("str_of_based_column", str_of_based_column))
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')


@setup_conf
def Search(con, cursor_r, scenario, dict_of_searching_var):
    list_of_commands = []
    for key, value in dict_of_searching_var.items():
        if(isinstance(value, list)):
            list_of_commands.append(key + " > " + value[0] + " AND " + key + " < " + value[1])
        else:
            list_of_commands.append(key + " LIKE " + value)
    commands = ' AND '.join(list_of_commands)
    try:
        take_sql_str_to_two_stream(cursor_r, additional_inf.set_command["presearch"][scenario] + commands)
        searching_values = cursor_r.fetchall()
    except psycopg2.Error as err:
        print(err.pgcode)
        print(f'WARNING:Error {err}')
    else:
        return searching_values

def take_sql_str_to_two_stream(cursor_r, sql_stream):
    print(sql_stream)
    cursor_r.execute(sql_stream)