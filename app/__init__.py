from flask import Flask
from flask_login import LoginManager
from app.database.models import Customer
from app.database import DB

URL = "sqlite:///app/database/Library.sql"

Library = DB( uri=URL)



def create_app():

    Library.init_db()
    
    app = Flask(__name__)
    engine = Library.engine
    app.config['SECRET_KEY'] = 'wbstbh'
    app.config['DATABASE'] = URL
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(customer_id):
        with Library.session() as s:
            return s.query(Customer).filter(Customer.id == customer_id).first()


            
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    from .librarian import admin as librarian_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(librarian_blueprint)


    return app





