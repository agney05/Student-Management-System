import sqlite3

def get_connection():
    return sqlite3.connect("students.db")

def add_student(name , roll_no , branch , semester):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    Insert into students(name, roll_no , branch , semester)
    values(?,?,?,?)
    """,(name,roll_no,branch,semester))

    conn.commit()

    conn.close()

def get_all_students():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("select * from students")

    students = cursor.fetchall()

    conn.close()

    return students

def delete_student(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("delete from students where id = ?",(student_id,))

    conn.commit()
    conn.close()

def update_student(student_id,name,roll_no,branch,semester):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    update students 
    set name = ? , 
    roll_no = ? ,
    branch = ? ,
    semester = ?
    where id = ?
    """,(name,roll_no,branch,semester,student_id))

    conn.commit()
    conn.close()

def get_student_by_id(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "select * from students where id = ?",(student_id,)
    ) 

    student = cursor.fetchone()

    conn.close()
    
    return student

def search_students(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    select * from students
    where name like ?
        or roll_no like ?
        or branch like ?
        or semester like ?
    """,
    (
        f"%{keyword}%",
        f"{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    students = cursor.fetchall()

    conn.close()

    return students

def verify_user(username,password):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    select * from users
    where username = ? 
    and password = ? 
    """,(username,password))

    user = cursor.fetchone()

    conn.close()

    return user

def count_students():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("select count(*) from students")

    count = cursor.fetchone()

    conn.close()

    return count

def count_students_branch():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    select branch,count(*) 
    from students 
    group by branch 
    """)
    
    branch_count = cursor.fetchall()

    conn.close()

    return branch_count


