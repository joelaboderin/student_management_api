from flask_restx import Resource, Namespace, fields, Model
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask import request
from ..models.course import Course
from ..models.student import Student
from http import HTTPStatus
from ..utils import db 


course_namespace=Namespace('course', description="Namespace for course")

student_model = Model('Student', {
    'id': fields.Integer(),
    'firstname': fields.String(),
    'surname': fields.String(),
    'email': fields.String()
})
course_model = course_namespace.model(
    'Course',{
        'id':fields.Integer(description="An ID"),
        'semester':fields.String(description="The current semester",
            required=True, enum=['FIRST','SECOND']
        ),
        'course_name':fields.String(required=True, description=" The course name"),
        'teacher':fields.String(required=True, description=" name of teacher"),
        'students': fields.List(fields.Nested(student_model))
    }
)
# add_students_request = Model('AddStudent', {
#     'students': fields.List(fields.Integer()),
# }
# )

@course_namespace.route('/courses/')
class StudentGetCreate(Resource):
    
    @course_namespace.marshal_with(course_model)
    @jwt_required()
    def get(self):
        
        """
             Get all Courses
        """
        courses=Course.query.all()

        return courses ,HTTPStatus.OK
    @course_namespace.expect(course_model)
    @course_namespace.marshal_with(course_model)
    @jwt_required()
    def post(self):
        """
        Register a Course
        """
        data=course_namespace.payload
        
        new_course = Course(
            teacher = data.get('teacher'),
            course_name = data.get('course_name'),
            semester = data.get('semester')
                 
            )
            
        new_course.save()
        
        
        return new_course , HTTPStatus.CREATED
    
@course_namespace.route('/course/<int:course_id>')
class GetUpdateDelete(Resource):
    
    @course_namespace.marshal_with(course_model)
    @jwt_required()
    def get(self,course_id):
        
        """
             Retrieve a course by id
        """
        course=Course.get_by_id(course_id)


        return course ,HTTPStatus.OK
    
    @course_namespace.expect(course_model)
    @course_namespace.marshal_with(course_model)
    @jwt_required()
    def put(self,course_id):
        
        """
             Update a course by id
        """
        
        course_to_update=Course.get_by_id(course_id)
        
        data=course_namespace.payload

       
        course_to_update.teacher=data['teacher']
        course_to_update.semester=data['semester']
        course_to_update.course_name=data['course_name']
        
       

        db.session.commit()

        return course_to_update ,HTTPStatus.OK
    
    @course_namespace.marshal_with(course_model)
    @jwt_required()
    def delete(self,course_id):
        
        """
             Delete a course
        """
        course_to_delete =Course.get_by_id(course_id)
        course_to_delete.delete()
        
        return course_to_delete ,HTTPStatus.OK
      
@course_namespace.route('/course/course/<int:course_id>')
class UpdateStudentStatus(Resource):
    
    def patch(self, student_id):
        """
            Update a Course status
        """
        pass
    
@course_namespace.route('/courses/<int:course_id>/students')
class ConnectingStudentCourse(Resource):
    
    # @course_namespace.expect(add_students_request)
    @course_namespace.marshal_with(course_model)
    @jwt_required()
    def post(self, course_id):
        """     
        Connecting student to courses
        """
        students = request.get_json()
        course = Course.get_by_id(course_id)
        for student_id in students['students']:
            student = Student.get_by_id(student_id)
            course.students.append(student)
        course.save()
        return course, HTTPStatus.CREATED
        
        
