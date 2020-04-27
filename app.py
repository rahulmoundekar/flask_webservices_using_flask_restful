from flask import Flask, request
from EmployeeService import get_employees, create_employee, update_employee, delete_employee, get_employee
from db.db import db
from flask_restful import Api, Resource
from flask_restful_swagger import swagger

from models.app_model import Employee

app = Flask(__name__)
app.secret_key = 'asrtarstaursdlarsn'
app.config.from_object('settings.Config')
api = Api(app)
api = swagger.docs(Api(app), apiVersion='0.1')

# initialization
db.init_app(app)


# http://docs.swagger.io/spec.html
class Employees(Resource):

    @swagger.operation(
        notes='This is Get Api for particular employee',
        responseClass=Employee.__name__,
        responseMessages=[
            {
                "code": 200,
                "message": "Loaded. "
            },
            {
                "code": 405,
                "message": "Invalid input"
            }
        ]
    )
    def get(self):
        print(get_employees())
        return get_employees()

    @swagger.operation(
        notes='This is POST Api',
        responseClass=Employee.__name__,
        nickname='upload',
        parameters=[
            {
                "name": "body",
                "description": "Insert Employee",
                "required": True,
                "allowMultiple": False,
                "dataType": Employee.__name__,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Loaded. "
            },
            {
                "code": 405,
                "message": "Invalid input"
            }
        ])
    def post(self):
        data = request.get_json()
        return create_employee(name=data['name'], email=data['email'], contact=data['contact'])

    @swagger.operation(
        notes='This is POST Api',
        responseClass=Employee.__name__,
        nickname='upload',
        parameters=[
            {
                "name": "body",
                "description": "Insert Employee",
                "required": True,
                "allowMultiple": False,
                "dataType": Employee.__name__,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {
                "code": 200,
                "message": "Loaded. "
            },
            {
                "code": 405,
                "message": "Invalid input"
            }
        ])
    def put(self):
        data = request.get_json()
        return update_employee(employee_id=data['id'], name=data['name'], email=data['email'], contact=data['contact'])


class EmployeeApi(Resource):

    @swagger.operation()
    def get(self, employee_id):
        return get_employee(employee_id)

    @swagger.operation()
    def delete(self, employee_id):
        return delete_employee(employee_id)


api.add_resource(EmployeeApi, '/employee/<int:employee_id>')
api.add_resource(Employees, '/employee')

# run always put in last statement or put after all @app.route
if __name__ == '__main__':
    app.run(host='localhost')

# manager.run()
