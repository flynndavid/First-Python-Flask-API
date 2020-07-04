from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

user_data = {
            "David":{
                "name":"David",
                "age":"22",
                "address":"1234 Street"
            },
            "Daniel":{
                "name":"Daniel",
                "age":"20",
                "address":"1234 Street"
            },
            "Andrew":{
                "name":"Andrew",
                "age":"18",
                "address":"1234 Street"
            }
            }
status = {
            "status": "Active",
        }

class Help(Resource):
    def get(self):
        help = {
            "Available REST APIs are": ["api/v1/ping","api/v1/user"]
        }
        return jsonify(help)

class Ping(Resource):
    def get(self):
        return jsonify(status)

class Employees(Resource):
    def __init__(self):
        print(request)
        print(request.authorization)
        print(request.args)

    def get(self, name=None):
        if request.args:
            if "name" not in request.args.keys():
                message  = {
                    "message": "Use <name> as query parameter",
                    "help":"/api/v1/user?name=<your_name>"
                } 
                return make_response(jsonify(message),404)
            uname = request.args.get('name')
            if uname in user_data.keys():
                return user_data.get(uname)
            message={
                        "Message": uname + " not found."
                    }
            return make_response(jsonify(message.get("Message")), 404)
        else:
            return make_response(jsonify(user_data),200)
    
    def post(self):
        print(request.args)
        pass

api.add_resource(Help,"/api/v1", "/api/v1/help")
api.add_resource(Ping,"/api/v1/ping")
api.add_resource(Employees,"/api/v1/user")

app.run(debug=True,port=5000,host="localhost")