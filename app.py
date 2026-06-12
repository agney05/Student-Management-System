from flask import Flask , render_template , request , redirect , session
from db_operations import (
    add_student ,
    get_all_students , 
    delete_student , 
    update_student , 
    get_student_by_id,
    search_students,
    verify_user,
    count_students,
    count_students_branch
)

from config import DATABASE , SECRET_KEY

app = Flask(__name__)

app.secret_key = SECRET_KEY

@app.route("/")
def home():

    if "logged_in" not in session:
        return redirect("/login")
    
    return render_template("index.html")

@app.route("/login")
def login_page():

    return render_template("login.html")

@app.route("/login" , methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = verify_user(username,password)

    if user:
        
        session["logged_in"] = True

        return redirect("/students")
    
    return "Invalid credentials"

@app.route("/logout")
def logout():

    session.pop("logged_in", None)

    return redirect("/login")

@app.route("/add_student" , methods=["POST"])
def add_student_route():
    name = request.form["student_name"]
    roll = request.form["roll_no"]
    branch = request.form["branch"]
    semester = request.form["semester"]

    add_student(name,roll,branch,semester)

    return "Student added successfully!"

@app.route("/students")
def view_students():

    if "logged_in" not in session:
        return redirect("/login")
    
    students = get_all_students()

    return render_template(
        "students.html",
        students=students
    )

@app.route("/delete/<int:id>")
def delete(id):

    if "logged_in" not in session:
        return redirect("/login")
    
    delete_student(id)

    return redirect("/students")

@app.route("/edit/<int:id>")
def edit_student(id):

    if "logged_in" not in session:
        return redirect("/login")

    student = get_student_by_id(id)

    return render_template(
        "edit_student.html",
        student=student
    )

@app.route("/update/<int:id>", methods=["POST"])
def update_student_route(id):

    if "logged_in" not in session:
        return redirect("/login")
    
    name = request.form["student_name"]
    roll = request.form["roll_no"]
    branch = request.form["branch"]
    semester = request.form["semester"]

    update_student(
        id,
        name,
        roll,
        branch,
        semester
    )

    return redirect("/students")

@app.route("/dashboard")
def dashboard():

    if "logged_in" not in session:
        return redirect("/login")
    
    count = count_students()
    branch_count = count_students_branch()

    return render_template(
        "dashboard.html",
        count = count,
        branch_count = branch_count
        )

@app.route("/about")
def about():
    return "About Student Portal"

@app.route("/help")
def help():
    return "Help Page"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"

@app.route("/square/<int:num>")
def square(num):
    return f"Square of {num} is {num**2}"

@app.route("/search" , methods = ["POST"])
def search():
    keyword = request.form["keyword"]

    students = search_students(keyword)

    return render_template(
        "students.html",
        students = students
    )

app.run(debug=True)
