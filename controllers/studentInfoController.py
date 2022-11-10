from flask import render_template, request, redirect
from constant import db
from controllers.loginController import checkUserLoggedIn 
import sqlite3

def getStudents():
    if not checkUserLoggedIn():
        return redirect('/login')
    
    students = []
    try:
        con = sqlite3.connect(db)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Student")
            students = cur.fetchall()
    except Exception as ex:
        print(ex)
    finally:
        if con:
            con.close()
    return students

def getQuizzes():
    if not checkUserLoggedIn():
        return redirect('/login')
    quizzes = []
    try:
        con = sqlite3.connect(db)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM quizzes")
            quizzes = cur.fetchall()
    except Exception as ex:
        print(ex)
    finally:
        if con:
            con.close()
    return quizzes

def dashboard():
    if not checkUserLoggedIn():
        return redirect('/login')
    students = getStudents()
    quizzes = getQuizzes()
    return render_template('dashboard.html', students=students, quizzes=quizzes)

def addStudentForm():
    if not checkUserLoggedIn():
        return redirect('/login')
    return render_template('studentForm.html')

def addStudent():
    if not checkUserLoggedIn():
        return redirect('/login')
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    if firstName == "" or lastName == "":
        return redirect('/student/add?error=Fields cannot be empty')
    try:
        con = sqlite3.connect(db)
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO Student(firstName, lastName) VALUES(?, ?);",(firstName, lastName))
        con.commit()
    except Exception as ex:
        print(ex)
    finally:
        if con:
            con.close()

    return redirect('/dashboard')

def addQuizForm():
    if not checkUserLoggedIn():
        return redirect('/login')
    return render_template('quizForm.html')

def addQuiz():
    if not checkUserLoggedIn():
        return redirect('/login')
    subject = request.form['subject']
    questions = request.form['questionCount']
    date = request.form['date']
    if subject == "" or questions == "" or date == "":
        return redirect('/quiz/add?error=Fields cannot be empty')
    try:
        con = sqlite3.connect(db)
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO Quizzes(subject, numberOfQuestion, date) VALUES(?, ?, ?);",(subject, questions, date))
        con.commit()
    except Exception as ex:
        print(ex)
    finally:
        if con:
            con.close()

    return redirect('/dashboard')

def studentScore(id):
    if not checkUserLoggedIn():
        return redirect('/login')
    studentResults = []
    try:
        con = sqlite3.connect(db)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM StudentResult WHERE studentId = ?",(id))
            studentResults = cur.fetchall()
    except Exception as ex:
        print(ex)
    finally:
        if con:
            con.close()
        
    return render_template('studentResult.html', studentResults=studentResults)


def addResultForm():
    if not checkUserLoggedIn():
        return redirect('/login')
    students = getStudents()
    quizzes = getQuizzes()
    return render_template('addResultForm.html', students=students, quizzes=quizzes)


def addResult():
    if not checkUserLoggedIn():
        return redirect('/login')
    studentId = request.form['student']
    subjectId = request.form['subject']
    grade = request.form['grade']
    if studentId == '' or subjectId == '' or grade == '':
        return redirect('/result/add?error=Fields cannot be empty')
    
    if int(grade) < 0 or int(grade) > 100:
        return redirect('/result/add?error=Grade should be between 0 - 100')
    try:
        con = sqlite3.connect(db)
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO StudentResult VALUES(?, ?, ?)", (studentId, subjectId, grade))
        con.commit()
    except Exception as ex:
        print(ex)
    finally:
        if con:
            con.close()
    
    return redirect('/dashboard')