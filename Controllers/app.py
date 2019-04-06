from flask import Flask, request, render_template, Response, jsonify
from Controllers.login import login_page

app = Flask(__name__)
app.register_blueprint(login_page)

if __name__ == '__main__':
    app.run()
