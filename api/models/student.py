from ..utils import db
from enum import Enum

class Courses(Enum):
    THERMODYNAMICS = 'thermodynamics'
    COMBUSTION = 'combustion'
    TURBINES = 'turbines'
    FLUID_MECHANICS = 'fluid_mechanics'
    
class StudentStatus(Enum):
    ACTIVE = 'active'
    PASSIVE = 'passive'
    INTERNING = 'interning'

class Student(db.Model):
    __tablename__='student'
    id = db.Column(db.Integer(), primary_key=True)
    course = db.Column(db.Enum(Courses), default = Courses.THERMODYNAMICS)
    student_status = db.Column(db.Enum(StudentStatus), default=StudentStatus.ACTIVE)
    teacher = db.Column(db.String(), nullable = False)
    gpa = db.Column(db.Integer, nullable=False)
    user = db.Column(db.Integer(), db.ForeignKey('users.id'))
    
    
    def __repr__(self):
        return f"<Student {self.username}>"
    