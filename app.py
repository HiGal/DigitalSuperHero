from flask import Flask
from flask_cors import CORS
from Controllers.login import login_page
from Controllers.marketplace import marketplace
from Controllers.my_requests import requests
from Controllers.board import kanban

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(login_page)
app.register_blueprint(marketplace)
app.register_blueprint(requests)
app.register_blueprint(kanban)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
