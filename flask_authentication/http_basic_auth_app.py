from flask_authentication import app,api
from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
user_data = {
    'john':'qwzx@#',
    'alice':'pomn$%'
}


@auth.verify_password
def verfiy_login(username,password):
    if username in user_data:
        return user_data[username]
    return None


class PrivateResourse(Resource):

    @auth.login_required()
    def get(self):
        return {"message":"Successful Get request to Private Resource"}, 200


api.add_resource(PrivateResourse,'/api/private')

if __name__ == "__main__":
    app.run(debug=True)