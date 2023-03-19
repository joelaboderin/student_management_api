from ..utils import db
from enum import Enum

    
class StudentStatus(Enum):
    ACTIVE = 'active'
    PASSIVE = 'passive'
    INTERNING = 'interning'

class Student(db.Model):
    __tablename__='students'
    id = db.Column(db.Integer(), primary_key=True)
    surname = db.Column(db.String(45), nullable=False)
    firstname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(50), nullable=False,unique=True)
  
    student_status = db.Column(db.Enum(StudentStatus), default=StudentStatus.ACTIVE)
    
    
    
    def __str__(self):
        return f"<Student {self.id}>"


    def save(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)
    
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
