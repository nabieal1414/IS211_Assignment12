from flask import Flask
from flask_migrate import Migrate 
from routes.login import login_bp
from routes.student import student_bp
from constant import secret_key

app=Flask(__name__)
app.secret_key=secret_key

app.register_blueprint(login_bp, url_prefix='/')
app.register_blueprint(student_bp, url_prefix='/')



if __name__ == '__main__':
    app.debug = True
    app.run()
