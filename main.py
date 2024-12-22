from flask import Flask

from config.config import Config
from database.init import init_db
from src.auth.controllers.auth import AuthController 
from src.user.controllers.user_controller import UserController
from src.main.controllers.main_controller import MainController


class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        init_db(self.app)
        self.register_routes()
        
        
    def register_routes(self):
        self.app.register_blueprint(MainController().main_bp,url_prefix="/")
        self.app.register_blueprint(AuthController().authBp, url_prefix="/auth")
        self.app.register_blueprint(UserController().user_bp, url_prefix="/user")
    
    
    def start(self):
        self.app.run(debug=True)

my_app = FlaskApp()
app = my_app.app

if __name__ == "__main__":
    my_app.start()