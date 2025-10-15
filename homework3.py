# import psycopg2

# conn = psycopg2.connect(
#     host="localhost",
#     database="postgres",
#     user="postgres",
#     password="1977",
#     port = 5432
# )




# def commit(func):
#     def wrapper(self,*args,**kwargs):
#         result = func(self,*args,**kwargs)
#         self.conn.commit()
#         return result
#     return wrapper


# class Person:
#     def __init__(self,conn):
#         self.conn = conn
#         self.cur = self.conn.cursor()

#     @commit
#     def insert_person(self, first_name, last_name,email,gender):
#         query = "INSERT INTO person(first_name, last_name,email,gender) VALUES (%s, %s,%s,%s)"
#         self.cur.execute(query, (first_name, last_name,email,gender))
#         print('INSERT 0 1')


# person = Person(conn)
# person.insert_person("Javlon", "Valiyev", "ali@mail.com", "male")




import psycopg2
from contextlib import contextmanager
from prettytable import PrettyTable

@contextmanager
def db_info():
    conn = psycopg2.connect(
        host = "localhost",
        database = "postgres",
        user = "postgres",
        password = "1977",
        port = 5432
    )
    cur = conn.cursor()
    try:
        yield cur
        conn.commit()
    finally:
        cur.close()
        conn.close()
    

with db_info() as cursor:
    cursor.execute('select *from person;')
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    table = PrettyTable()
    table.field_names = columns


    for row in rows:
        table.add_row(row)

    print(table)



# def permission_decorator(func):
#     def wrapper(user, *args, **kwargs):
#          if user.get("role") == "admin":
#             return func(user, *args, **kwargs)
#          else:
#             print("Sizda bu amalni bajarishga ruxsat yo'q!")
#     return wrapper


# @permission_decorator
# def create_post(user):
#     print(" Post yaratildi!")

# @permission_decorator
# def delete_post(user):
#     print(" Post o‘chirildi!")


# admin_user = {"username": "Ali", "role": "admin"}
# normal_user = {"username": "Vali", "role": "user"}

# create_post(admin_user)
# create_post(normal_user)  