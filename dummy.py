import sqlite3

connect = sqlite3.connect("student.db")
cursor = connect.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY,
        student_name TEXT NOT NULL,
        father_name TEXT NOT NULL,
        course_name TEXT NOT NULL
    )
    """
)


def data_entry():
    value = "next"
    while value != "stop":
       try:
         student_id = int(input("\n Student id:"))
       except ValueError e  
        
        student_name = str(input("\n Student name:"))
        father_name = str(input("\n Father name:"))
        course_name = str(input("\n Course name:"))
        student_list = [student_id, student_name, father_name, course_name]

        cursor.execute(
            "INSERT INTO student (id, student_name, father_name, course_name) VALUES (?, ?, ?, ?)",
            student_list
        )
        connect.commit()
        value = input("if stop type 'stop' other wise anykey:")


def main():
    data_entry()


if __name__ == "__main__":
    main()