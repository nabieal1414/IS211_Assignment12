from flask import Blueprint, render_template
from controllers.studentInfoController import dashboard, addStudentForm, addStudent, addQuizForm, addQuiz,studentScore, addResultForm, addResult

student_bp = Blueprint('student_bp', __name__,  template_folder='templates')

student_bp.route('/dashboard', methods=['GET'])(dashboard)
student_bp.route('/student/add', methods=['GET'])(addStudentForm)
student_bp.route('/student/add', methods=['POST'])(addStudent)
student_bp.route('/quiz/add', methods=['GET'])(addQuizForm)
student_bp.route('/quiz/add', methods=['POST'])(addQuiz)
student_bp.route('/student/<id>', methods=['GET'])(studentScore)
student_bp.route('/result/add', methods=['GET'])(addResultForm)
student_bp.route('/result/add', methods=['POST'])(addResult)