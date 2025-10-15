# __enter__
# __exit__


# with open('lesson3/data.txt') as f:
#     print(f.read())

from dataclasses import dataclass


# @dataclass
# class MyManager:
#     def __init__(self): # 1
#         print('Init method called')
    
#     def __enter__(self):
#         print('Enter method called') # 2
    
#     def __exit__(self,exc_type, exc_value, tb):
#         print('Exit method called') # 4
        

# with MyManager() as obj:
#     print('Body logic called') # 3


# @dataclass 
# class FileManager:
#     file_path : str
#     mode : str = 'r'
#     file : str | None = None
    
    
#     def __enter__(self):
#         self.file = open(self.file_path,self.mode)
#         return self.file
    
    
#     def __exit__(self,exc_type, exc_value, tb):
#         if self.file:
#             if not self.file.closed:
#                 self.file.close()
               
               
               
# with FileManager('data.txt','w') as file:
#     file.write('Tom\n')  
#     file.write('John')


# db_info = {
#     'database' : 'postgres',
#     "user" : "postgres",
#     "password" : '1977',
#     "host" : "localhost",
#     "port" : 5432
# }

# # from lesson1.db_info import *
# import psycopg2
# from contextlib import contextmanager

# @contextmanager
# def postgres_connection(db_info : dict):
#     conn = None
#     cur = None
#     try:
#         conn = psycopg2.connect(**db_info)
#         cur = conn.cursor()
#         yield cur  
#         conn.commit()
#     except Exception as e:
#         if conn:
#             conn.rollback()
#             print("⚠️ Xato! Rollback bajarildi:", e)
#         raise
#     finally:
#         if cur:
#             cur.close()
#         if conn:
#             conn.close()


# # with postgres_connection(db_info) as cur:
# #     insert_data_query = '''insert into person(first_name,last_name,age,email)
# #     values ('test','test',25,'test');'''
# #     cur.execute(insert_data_query)



# @dataclass
# class Person:
#     first_name : str
#     last_name : str
#     email :  str | None = None
#     gender : str | None = None
  
#     def save(self):
#         with postgres_connection(**db_info) as cur:
#             with cur.execute() as cur:
#                 insert_data_query = '''
#                     insert into person(first_name,last_name,email,gander) 
#                     values (Jamoldin,Yusubjonov,jhdhwjdwdj@gmail.com,Male);
#                 '''
#                 cur.execute(insert_data_query,(self.first_name,self.last_name,self.email,self.gender))
#                 print('INSERT 0 1')
    


# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print('Funksiya ishlashidan oldin ....')
#         func(*args,**kwargs)
#         print('Funksiya ishlagandan keyin ....')
        
        
#     return wrapper



# @my_decorator
# def say_hello():
#     print('Hello')
    
    
# say_hello()
# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print('Funksiya ishlashidan oldin ....')
#         result = func(*args,**kwargs)
#         print('Funksiya ishlagandan keyin ....')
#         return result
    
#     return wrapper
    



# @my_decorator
# def greeting(name : str):
#     return f"Hello {name}"


# print(greeting('John'))


# pow(2,5)


# import time

# def timing(func):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         result = func(*args,**kwargs)
#         end_time = time.time()
#         print(f'{end_time - start_time} shuncha vaqt ketdi...')
#         return result
#     return wrapper



# @timing
# def pow(a,b):
#     return a ** b


# result = pow(124,231)
# print(result)


# @login_required
# def create_post(request):
#     pass

# def commit():
#     pass

# @commit
# def insert_person():
#     pass
    # conn.commit()






    # rows = cursor.fetchall()
    # columns = [desc[0] for desc in cursor.description]  # ustun nomlari

    # table = PrettyTable()
    # table.field_names = columns  # ustun sarlavhalari

    # for row in rows:
    #     table.add_row(row)

    # print(table)

# from contextlib import contextmanager
# import psycopg2

# @contextmanager
# def get_db():
#     conn = psycopg2.connect(
#         host="localhost",
#         database="postgres",
#         user="postgres",
#         password="1234"
#     )
#     cur = conn.cursor()
#     try:
#         yield cur
#         conn.commit()
#     finally:
#         cur.close()
#         conn.close()

# with get_db() as cursor:
#     cursor.execute("SELECT * FROM person;")
#     print(cursor.fetchall())