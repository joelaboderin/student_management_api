from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required,get_jwt_identity
from ..models.student import Student
from http import HTTPStatus
from ..utils import db 


student_namespace=Namespace('student', description="Namespace for student")

student_model = student_namespace.model(
    'Student',{
        'id':fields.Integer(description="An ID"),
        'student_status':fields.String(description="The status of the Student",
            required=True, enum=['ACTIVE','PASSIVE','INTERNING']
        ),
        'surname':fields.String(required=True, description="A surname"),
        'firstname':fields.String(required=True, description="firstname"),
        'email': fields.String(required=True,description="An email")
    }
)

@student_namespace.route('/students/')
class StudentGetCreate(Resource):
    
    @student_namespace.marshal_with(student_model)
    @jwt_required()
    def get(self):
        
        """
             Get all Students
        """
        students=Student.query.all()

        return students ,HTTPStatus.OK
    @student_namespace.expect(student_model)
    @student_namespace.marshal_with(student_model)
    @jwt_required()
    def post(self):
        """
        Register a Student
        """
        data=student_namespace.payload
        
        new_student = Student(
            surname = data.get('surname'),
            firstname = data.get('firstname'),
            email = data.get('email'),
            student_status = data.get('student_status')
                 
            )
            
        new_student.save()
        
        
        return new_student , HTTPStatus.CREATED
    
@student_namespace.route('/student/<int:student_id>')
class GetUpdateDelete(Resource):
    
    @student_namespace.marshal_with(student_model)
    @jwt_required()
    def get(self,student_id):
        
        """
             Retrieve a student by id
        """
        student=Student.get_by_id(student_id)


        return student ,HTTPStatus.OK
    
    @student_namespace.expect(student_model)
    @student_namespace.marshal_with(student_model)
    @jwt_required()
    def put(self,student_id):
        
        """
             Update a student by id
        """
        
        student_to_update=Student.get_by_id(student_id)
        
        data=student_namespace.payload

       
        student_to_update.email=data['email']
        student_to_update.student_status=data['student_status']
        student_to_update.firstname=data['firstname']
        student_to_update.surname=data['surname']
       

        db.session.commit()

        return student_to_update ,HTTPStatus.OK
    
    @student_namespace.marshal_with(student_model)
    @jwt_required()
    def delete(self,student_id):
        
        """
             Delete a student
        """
        student_to_delete =Student.get_by_id(student_id)
        student_to_delete.delete()
        
        return student_to_delete ,HTTPStatus.OK
      
@student_namespace.route('/student/status/<int:student_id>')
class UpdateStudentStatus(Resource):
    
    def patch(self, student_id):
        """
            Update a student's status
        """
        pass