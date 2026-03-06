from flask import Flask,request
from flask_restful import Api,Resource
app = Flask(__name__)
api = Api(app)
users=[]
class UserList(Resource):
    def get(self):
        return {"users":users},200
    def post(self):
        data = request.get_json()
        users.append(data)
        return{"message":"users added",
               "users":data},201
    
class User(Resource):
    def get(self,user_id):
        for user in users:
            if user["id"] ==user_id:
                return user,200
        return {"message":"user not found"},404
    
    def put(self,user_id):
        data = request.get_json()
        for user in users:
            if user["id"]==user_id:
                user["name"]=data["name"]
                return {"message":"user updated"},200
        return {"message":"user not found"},404
    
    def delete(self,user_id):
        for user in users:
            if user["id"]==user_id:
                users.remove(user)
                return{"message":"user deleted"},200
        return {"message":"user not found"},404
    
api.add_resource(UserList,"/users")
api.add_resource(User,"/users/<int:user_id>")
if __name__ =="__main__":
    app.run(debug=True)



