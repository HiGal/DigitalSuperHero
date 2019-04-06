from flask import Flask, Blueprint, Response, request
from Models.User import User

login_page = Blueprint('login', __name__)


def hash_password(password: str) -> str:
    from hashlib import md5
    return md5(password.encode()).hexdigest()


@login_page.route('/')
def hello_world():
    return 'Hello World!'


@login_page.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        data['password'] = hash_password(data['password'])
        print(data)
        user = User(data['username'], data['password'])
        # session['user'] = (data['username'], data['password'])
        if user.verify():
            return Response('/profile')
        else:
            return Response("Username or Password incorrect")
    return Response('login.html')


@login_page.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User()
        data = request.get_json(silent=True)
        name = data['name']
        sname = data['sname']
        email = data['email']
        bdate = data['bdate']
        if data['password'] == data['cpassword']:
            password = hash_password(data['password'])
            user.register(email, password, name, sname, email, bdate)
            return Response("Account successfully created")
        else:
            return Response("Password are not the same!")
    return Response('registration.html')
