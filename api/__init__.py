from flask import Flask
from flask_restx import Api
from .student.views import student_namespace
from .auth.views import auth_namespace
from .config.config import config_dict
from .utils import db
from .models.student import Student
from .models.users import User
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


    
def create_app(config=config_dict['dev']):
    app=Flask(__name__)
    
    app.config.from_object(config)
    
   
    
    api=Api(app)
    
    api.add_namespace(student_namespace)
    api.add_namespace(auth_namespace, path='/auth')
    
    db.init_app(app)
    migrate = Migrate(app,db)
    jwt = JWTManager(app)

    
    @app.shell_context_processor
    def make_shell_context():
        return{
            
            'db':db,
            'User': User,
            'Student': Student
        }
    
    return app