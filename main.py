from db import ScopedSession, get_db_session
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask import Flask
from models.User import User
from routes import bp


app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xd4\xc5\xf2\xae\xaa\xb7\xc7\xd9}\xf3}\xebHG\xa4\x96'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.register_blueprint(bp)
db = get_db_session()
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'routes.login'

migrate = Migrate(app, ScopedSession())


@login_manager.user_loader
def load_user(user_id):
    session = ScopedSession()
    return session.query(User).filter(User.id == int(user_id)).first()


@app.before_request
def create_session():
    ScopedSession()


@app.teardown_appcontext
def shutdown_session(response_or_exc):
    ScopedSession.remove()


if __name__ == '__main__':
    app.run(debug=True)