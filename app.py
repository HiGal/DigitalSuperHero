from flask import Flask

from login import login_page
from marketplace import marketplace

app = Flask(__name__)
app.register_blueprint(login_page)
app.register_blueprint(marketplace)

if __name__ == '__main__':
    app.run()
