from flask import Flask
from flask_cors import CORS
from Controllers.login import login_page
from Controllers.marketplace import marketplace

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(login_page)
app.register_blueprint(marketplace)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
