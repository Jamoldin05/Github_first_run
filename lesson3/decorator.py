

import psycopg2
from dataclasses import dataclass

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
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print('Funksiya ishlashidan oldin ....')
        result = func(*args,**kwargs)
        print('Funksiya ishlagandan keyin ....')
        return result
    
    return wrapper
    



@my_decorator
def greeting(name : str):
    return f"Hello {name}"


print(greeting('John'))


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



# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print('Salom')
#         result = func(*args,**kwargs)
#         print('Hush kelibsz !')
#         return result
#     return wrapper


# @my_decorator
# def terminal(name : str):
#     print(f"{name} ")

# print(terminal('Jamoldin'))