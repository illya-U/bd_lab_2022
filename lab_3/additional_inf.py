set_command = {
        "random":
            {
              "train":"INSERT INTO train (parametrs) SELECT timestamp '1970-01-10 20:00:00' + random()* (timestamp '2033-01-20 20:00:00' - timestamp '1970-01-10 10:00:00'),timestamp '1970-01-10 20:00:00'+ random() * (timestamp '1970-01-20 20:00:00' - timestamp '1970-01-20 20:00:00'),chr(trunc(65+random()*25)::int)",
              "railcar":"INSERT INTO railcar (parametrs) SELECT chr(trunc(65+random()*25)::int), timestamp '1970-01-10 20:00:00'+ random() * (timestamp '2033-01-20 20:00:00' - timestamp '1970-01-10 10:00:00'),id_train From train order by random() limit 1",
              "ticket":"INSERT INTO ticket (parametrs) SELECT trunc(random()*1000)::int,trunc(random()*1000)::int,chr(trunc(65+random()*25)::int),id_railcar FROM railcar order by random() limit 1"
            },
        "delete":"delete FROM table_name WHERE str_of_based_column",
        "add_inf":"INSERT INTO table_name (parametrs) VALUES (values)",
        "upd_inf":"UPDATE table_name SET str_of_updating_column WHERE str_of_based_column;",
        "inf":"SELECT param FROM table",
        "presearch":
            [
                "SELECT * FROM train, ticket WHERE ",
                "SELECT id_railcar,id_ticket,material,cost FROM railcar, ticket WHERE ",
                "SELECT * FROM railcar,ticket,train WHERE "
            ]
    }

parametrs = {
                "train":[("id_train","int"),("departure_time","time"),("arrival_time","time"),("route","str")],
                "railcar":[("id_railcar","int"),("type_railcar","str"),("year_start_use_railcar","time"),("train","int")],
                "ticket":[("id_ticket","int"),("cost","int"),("seat_in_the_train","int"),("material","str"),("railcar","int")]
            }

randomvalue_type = {
    'int': "trunc(random()*1000)::int,trunc(random()*1000)::int",
    'data': "timestamp '1970-01-10 20:00:00'+ random() * (timestamp '1970-01-20 20:00:00' - timestamp '1970-01-20 20:00:00')",
    'str': "chr(trunc(65+random()*25)::int)"
                   }