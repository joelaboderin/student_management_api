from flask_restx import Resource, Namespace

student_namespace=Namespace('student', description="Namespace for student")


@student_namespace.route('/student')
class StudentGetCreate(Resource):
    
    def get(self):
        
        """
             Get all Student
        """
        pass
    
    def post(self):
        """
        Register a Student
        """
        pass
@student_namespace.route('/student/<int:student_id>')
class GetUpdateDelete(Resource):
    
    def get(self,student_id):
        
        """
             Retrieve a student by id
        """
        pass
    def put(self,student_id):
        
        """
             Update a student by id
        """
        pass
    def delete(self,student_id):
        
        """
             Delete a student
        """
        pass
@student_namespace.route('/user/<int:user_id>/student/<int:student_id>')
class GetSpecificOrderByUser(Resource):
    
    def get(self,user_id, student_id):
        """
            Get a user's specific student information
        """
        pass
      
@student_namespace.route('/student/status/<int:student_id>')
class UpdateStudentStatus(Resource):
    
    def patch(self, student_id):
        """
            Upddate a student's status
        """
        pass