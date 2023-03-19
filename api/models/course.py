from ..utils import db
from enum import Enum

course_student = db.Table('course_student',
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('grade', db.Integer)
)
class Semester(Enum):
    FIRST = 'first'
    SECOND = 'second'

class Course(db.Model):
    __tablename__='courses'
    id = db.Column(db.Integer(), primary_key=True)
    course_name = db.Column(db.String(45), nullable=False)
    teacher = db.Column(db.String(45), nullable=False)
    semester = db.Column(db.Enum(Semester), default=Semester.FIRST)
    students = db.relationship('Student', secondary=course_student, lazy='subquery', backref='courses')
    
    
    
    def __str__(self):
        return f"<Course {self.id}>"


    def save(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)
    
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()