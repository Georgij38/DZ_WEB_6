import sqlite3
from faker import Faker
import random

# Ініціалізуємо Faker для генерації випадкових даних
fake = Faker()

# Підключаємося до бази даних SQLite
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створюємо таблиці
cursor.execute('''drop table if exists students;''')
cursor.execute('''CREATE TABLE students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER)''')

cursor.execute('''drop table if exists groups;''')
cursor.execute('''CREATE TABLE groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT)''')

cursor.execute('''drop table if exists teachers;''')
cursor.execute('''CREATE TABLE teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT)''')

cursor.execute('''drop table if exists subjects;''')
cursor.execute('''CREATE TABLE subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER)''')

cursor.execute('''drop table if exists grades ;''')
cursor.execute('''CREATE TABLE grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date TEXT)''')

# Додаємо дані до таблиць
for _ in range(3):  # Додаємо 3 групи
    group_name = fake.word()
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))
    group_id = cursor.lastrowid
    for _ in range(random.randint(20, 50)):  # Додаємо випадкову кількість студентів до кожної групи
        student_name = fake.name()
        cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (student_name, group_id))

for _ in range(3):  # Додаємо 3 викладачів
    teacher_name = fake.name()
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher_name,))

for _ in range(5):  # Додаємо 5 предметів
    subject_name = fake.word()
    teacher_id = random.randint(1, 3)  # Випадково вибираємо викладача для предмета
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject_name, teacher_id))

for student_id in range(1, 51):  # Додаємо оцінки для кожного студента з усіх предметів
    for subject_id in range(1, 6):
        grade = random.randint(0, 100)  # Випадкова оцінка від 0 до 100
        date = fake.date()
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                       (student_id, subject_id, grade, date))

# Зберігаємо зміни
conn.commit()

# Вибірка даних

with open('query_1.sql', 'r') as file:
    sql_query1 = file.read()

cursor.execute(sql_query1)

results = cursor.fetchall()
print('5 студентів із найбільшим середнім балом з усіх предметів')
for row in results:
    print(row)


subject_id = 1
with open('query_2.sql', 'r') as file:
    sql_query2 = file.read()
cursor.execute(sql_query2, (subject_id,))
results = cursor.fetchall()
print(f'студента із найвищим середнім балом з певного предмета, {subject_id}')
print(results)

subject_id = 1  # Замініть 1 на ідентифікатор певного предмета
with open('query_3.sql', 'r') as file:
    sql_query3 = file.read()
cursor.execute(sql_query3, (subject_id,))
result = cursor.fetchall()
print("Середній бал у групах з предмета з ID", subject_id)
print(result)

with open('query_4.sql', 'r') as file:
    sql_query4 = file.read()
cursor.execute(sql_query4)
result = cursor.fetchone()
print("Середній бал на потоці:")
print(result)


teacher_id = 1  # Замініть 1 на ідентифікатор певного викладача
with open('query_5.sql', 'r') as file:
    sql_query5 = file.read()
cursor.execute(sql_query5, (teacher_id,))
result = cursor.fetchall()
print("Курси, які читає викладач з ID", teacher_id)
print(result)

group_id = 3  # Замініть 1 на ідентифікатор певної групи
with open('query_6.sql', 'r') as file:
    sql_query6 = file.read()
cursor.execute(sql_query6, (group_id,))
result = cursor.fetchall()
print("Список студентів у групі з ID", group_id)
for row in result:
    print(row[0])


group_id = 2  # Замініть 1 на ідентифікатор певної групи
subject_id = 1  # Замініть 1 на ідентифікатор певного предмета

with open('query_7.sql', 'r') as file:
    sql_query7 = file.read()
cursor.execute(sql_query7, (group_id, subject_id))
result = cursor.fetchall()
print("Оцінки студентів у групі з ID", group_id, "з предмета з ID", subject_id)
print(result)


teacher_id = 2  # Замініть 1 на ідентифікатор певного викладача

with open('query_8.sql', 'r') as file:
    sql_query8 = file.read()
cursor.execute(sql_query8, (teacher_id,))
result = cursor.fetchone()
print("Середній бал, який ставить викладач з ID", teacher_id, "зі своїх предметів:")
print(result)


student_id = 1  # Замініть 1 на ідентифікатор певного студента

# Знайти всі предмети, які відвідує студент
with open('query_9.sql', 'r') as file:
    sql_query9 = file.read()
cursor.execute(sql_query9, (student_id,))
result = cursor.fetchall()

# Вивести список курсів, які відвідує студент
print("Список курсів, які відвідує студент з ID", student_id)
for row in result:
    print(row[0])

student_id = 1  # Замініть 1 на ідентифікатор певного студента
teacher_id = 1  # Замініть 1 на ідентифікатор певного викладача


with open('query_9.sql', 'r') as file:
    sql_query9 = file.read()
cursor.execute(sql_query9, (student_id,))
student_subjects = cursor.fetchall()

with open('query_10.sql', 'r') as file:
    sql_query10 = file.read()
cursor.execute(sql_query10, (teacher_id, student_id))
result = cursor.fetchall()

# Виведемо список курсів, які певний студент відвідує, що читає певний викладач
print("Список курсів, які студент з ID", student_id, "відвідує, що читає викладач з ID", teacher_id)
for row in result:
    print(row[0])

# Закриваємо з'єднання з базою даних
conn.close()
