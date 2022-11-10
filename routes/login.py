from flask import Blueprint, render_template
from controllers.loginController import login,verfiyCredentails, logout

login_bp = Blueprint('login_bp', __name__,  template_folder='templates')

login_bp.route('/login', methods=['GET'])(login)
login_bp.route('/verify', methods=['POST'])(verfiyCredentails)
login_bp.route('/logout', methods=['GET'])(logout)