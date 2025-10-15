import psycopg2

from  prettytable import PrettyTable




db_info = {
    'database' : 'postgres',
    "user" : "postgres",
    "password" : '1977',
    "host" : "localhost",
    "port" : 5432
}

conn = psycopg2.connect(**db_info)

cur = conn.cursor()


# class Person:
#     def __init__ (self,first_name,last_name,age,country):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.country = country


#     def get_info(self):
#         return f"Name : {self.first_name}{self.last_name} Age : {self.age} Country : {self.country}"


#     def save_person(self,name,age,country):
        

# set_schenma = ''' set search_path to texnomart'''


# cur.execute(set_schenma)

# print("Schema texnomart tanlandi!")

# conn.commit()
# cur.close()
# conn.close()


# select_users_query = ''' select * from person where gender = 'Male' ;'''

# cur.execute(select_users_query)

# rows = cur.fetchall()
# columns = [desc[0] for desc in cur.description]

# table = PrettyTable()
# table.field_names = columns

# for row in rows:
#     table.add_row(row)

# print(table)

# cur.close()
# conn.close()

# post_data = cur.fetchall()

# print(post_data)


create_table_query = """
CREATE TABLE IF NOT EXISTS person(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(250) NOT NULL,
    last_name VARCHAR(250) NOT NULL,
    age INT CHECK (age > 0)
);
"""

cur.execute(create_table_query)
conn.commit()

print("Jadval muvaffaqiyatli yaratildi!")

cur.close()
conn.close()



def save_person(first_name, last_name, age):

    query = "INSERT INTO PERSON (first_name, last_name, age) VALUES (%s, %s,%s)"
    cur.execute(query,(first_name, last_name, age))
    conn.commit()
    cur.close()
    conn.close()

    print(f"{first_name} ismli person yaratildi")

save_person('Jamoldin', 'Yusufjonov', 20)



def get_all_person():
    cur.execute("SELECT *FROM person")
    people = cur.fetchall()

    cur.close()
    conn.close()
    return people

print(get_all_person())


def get_person(person_id):
    query = "SELECT * FROM person WHERE id = %s"
    cur.execute(query, (person_id,))  
    result = cur.fetchone()

    cur.close()
    conn.close()
    return result

print(get_person(1))
