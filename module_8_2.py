from peewee import*
import sqlite3


conn = SqliteDatabase('student.sqlite')


class Student(Model):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')
    
    class Meta:
        database = conn
       
class Courses(Model):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    time_start = DateTimeField(column_name='time_start')
    time_end = DateTimeField(column_name='time_end')
    
    class Meta:
        database = conn
            
class Student_Courses(Model):
    student_id = ForeignKeyField(Student, to_field="id", column_name='student_id')
    course_id = ForeignKeyField(Courses, to_field="id", column_name='course_id')
    
    class Meta:
        database = conn
        

# Student.create_table()
# Courses.create_table()
# Student_Courses.create_table()

# st = Student(name = "Max", surname = "Brooks", age=24 , city = "Spb")
# st.save()
# st = Student(name = "John", surname = "Stones", age=15 , city = "Spb")
# st.save()
# st = Student(name = "Andy", surname = "Wings", age=45 , city = "Manchester")
# st.save()
# st = Student(name = "Kate", surname = "Brooks", age=34 , city = "Spb")
# st.save()

# cour = Courses(name = "python", time_start = "21.07.2021", time_end = "21.08.2021")
# cour.save()
# cour = Courses(name = "java", time_start = "13.07.2021", time_end = "16.08.2021")
# cour.save()

# st_cour = Student_Courses(student_id = 1, course_id = 1)
# st_cour.save()
# st_cour = Student_Courses(student_id = 2, course_id = 1)
# st_cour.save()
# st_cour = Student_Courses(student_id = 3, course_id = 1)
# st_cour.save()
# st_cour = Student_Courses(student_id = 4, course_id = 2)
# st_cour.save()

# rows=Student.select().where (Student.age>30)
# for student in rows:
#     print ("name: {} age: {}".format(student.name, student.age))

# rows2 = Student.select().join(Student_Courses).join(Courses).where(Courses.name == 'python')
# for student in rows2:
#     print("name: {} age: {} city: {}".format(student.name, student.age, student.city))

# rows3 = Student.select().join(Student_Courses).join(Courses).where((Student.city == 'Spb') and (Courses.name == 'python'))
# for student in rows3:
#     print("name: {} age: {}".format(student.name, student.age))

conn.commit()
conn.close()