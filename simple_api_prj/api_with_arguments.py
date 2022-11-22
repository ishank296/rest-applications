from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

employee_dict = {
 100 : {'name': 'Roger Bane'
        ,'desg' : 'Sales Rep'
        ,'salary' : 5400.00
        },
 200 : {'name':'Alice Williams'
        ,'desg' : 'HR consulant'
        ,'salary': 6700.44
     },
300 : {'name': 'Jene Walker'
       ,'desg': 'It Engineer'
       ,'salary' : 8000.00
    }
}


class Employee(Resource):

    def get(self,id :int):
        return employee_dict[id]


class SalesEmployee(Resource):

    def get(self):
        return {key:value for key,value in employee_dict.items()
                if 'sales' in value['desg'].lower()
                }


api.add_resource(Employee,'/employee/<int:id>')
api.add_resource(SalesEmployee,'/sales')

if __name__ == "__main__":
    app.run(debug=True)