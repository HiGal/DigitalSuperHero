from flask import Flask, Blueprint, Response, request
from Models.UserContractor import UserContractor
from Models.UserCustomer import UserCustomer
from Models.UserCompany import UserCompany

login_page = Blueprint('login', __name__)


@login_page.route('/')
def hello_world():
    return 'Hello World!'


@login_page.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        if data['user_type'] == 'contractor':
            user = UserContractor(data['email'], data['password'])
            if user.verify():
                return Response('/profile')
            else:
                return Response("Username or Password incorrect")
        elif data['user_type'] == 'customer':
            user = UserCustomer(data['email'], data['password'])
            if user.verify():
                return Response('/profile')
            else:
                return Response("Username or Password incorrect")
        elif data['user_type'] == 'company':
            user = UserCompany(data['email'], data['password'])
            if user.verify():
                return Response('/profile')
            else:
                return Response("Username or Password incorrect")
    return Response('login.html')


@login_page.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        if data['password'] == data['cpassword']:
            if data['user_type'] == 'contractor':
                user = UserContractor(data['email'], data['password'])
                phone = data['phone']
                inn = data['inn']
                company_name = data['company_name']
                reg_date = data['reg_date']
                user.register(data['email'], data['password'], phone, inn, company_name, reg_date)
                return Response("Account successfully created")
            elif data['user_type'] == 'customer':
                user = UserCustomer(data['email'], data['password'])
                phone = data['phone']
                name = data['name']
                surname = data['surname']
                midname = data['midname']
                user.register(data['email'], data['password'], phone, name, surname, midname)
                return Response("Account successfully created")
            elif data['user_type'] == 'company':
                user = UserCompany(data['email'], data['password'])
                company_name = data['company_name']
                inn = data['inn']
                user.register(data['email'], data['password'], company_name, inn)
                return Response("Account successfully created")
        else:
            return Response("Password are not the same!")

    return Response('registration.html')
