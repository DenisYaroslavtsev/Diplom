from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from Flask.backend.db import get_db
from Flask.models.models import User
from schemas import UserResponse, CreateUser
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'very Very very Secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_user():
    if request.method == 'POST':
        user = UserResponse(**request.form)

        if not user.email:
            flash("Email должен быть введён обязательно!", "error")
            return redirect(url_for('home'))

        if user.username == user.password:
            flash("Пароль не должен совпадать с логином!", "error")
            return redirect(url_for('home'))

        if user.password != user.repeat_password:
            flash("Пароли не совпадают!", "error")
            return redirect(url_for('home'))

        db: Session = get_db()
        existing_user = db.query(User).filter_by(username=user.username).first()

        if existing_user:
            flash("Данный логин уже занят", "error")
            return redirect(url_for('home'))

        existing_email = db.query(User).filter_by(email=user.email).first()
        if existing_email:
            flash("Данный email уже занят", "error")
            return redirect(url_for('home'))

        hashed_password = generate_password_hash(user.password)
        db_user = User(username=user.username, password=hashed_password, email=user.email, birth_day=user.birth_date)
        db.add(db_user)
        db.commit()

        return redirect(url_for('login_user'))

    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login_user():
    if request.method == 'POST':
        user_data = CreateUser(**request.form)
        db_session: Session = next(get_db())
        db_user = db_session.query(User).filter_by(email=user_data.email).first()

        if not db_user or not check_password_hash(db_user.password, user_data.password):
            flash("Неправильно введён email или пароль", "error")
            return redirect(url_for('login_user'))

        flash(f"Добро пожаловать {db_user.username}", "success")
        return redirect(url_for('some_protected_route'))

    return render_template('login.html')


if __name__ == '__main__':
    app.run()
