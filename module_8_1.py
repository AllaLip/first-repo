import sqlite3 as sq
import datetime

students1 = [
    (1, 'Max', 'Brooks', 24, 'Spb'),
    (2, 'John', 'Stones', 15, 'Spb'),
    (3, 'Andy', 'Wings', 45, 'Manhester'),
    (4,'Kate', 'Brooks', 34, 'Spb')
     ]

courses1 = [(1, 'python', datetime.date(2021, 7, 21), datetime.date(2021, 8, 21)),
           (2, 'java', datetime.date(2021, 7, 13), datetime.date(2021, 8, 16))
           ]

student_courses = [(1, 1),
                   (2, 1),
                   (3, 1),
                   (4, 2)
                   ]


with sq.connect('students2.db') as con:
    cur = con.cursor() 
    
    cur.executescript('''CREATE TABLE IF NOT EXISTS students1(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        surname TEXT,
        age INTEGER,
        city TEXT);
    
    CREATE TABLE IF NOT EXISTS courses1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        time_start DATETIME,
        time_end DATETIME
        );
    
    CREATE TABLE IF NOT EXISTS student_courses(
        student_id INTEGER, 
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students1(id),
        FOREIGN KEY (course_id) REFERENCES courses1(id)
        );''')
    
    #cur.executemany("INSERT INTO students1 VALUES (?, ?, ?, ?, ?)", students1)
    #cur.executemany("INSERT INTO courses1 VALUES (?, ?, ?, ?)", courses1)
    #cur.executemany("INSERT INTO student_courses VALUES (?, ?)", student_courses)
    
    #cur.execute("SELECT * FROM  students1  WHERE age > 30")
    #print(cur.fetchall())
    
    
    #cur.execute('''SELECT students1.name, students1.surname FROM students1 JOIN student_courses ON student_courses.student_id = students1.id JOIN courses1 ON student_courses.course_id = courses1.id WHERE courses1.name = "python" ''')
    #print(cur.fetchall())
    
    cur.execute('''SELECT students1.name, students1.surname FROM students1 JOIN student_courses ON student_courses.student_id = students1.id JOIN courses1 ON student_courses.course_id = courses1.id WHERE courses1.name = "python" AND students1.city = "Spb" ''')
    print(cur.fetchall())
    
    