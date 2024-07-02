from flask_restful import Resource, Api 
from flask import jsonify,request 

# todos = {"1":"first todo","2":"second todo"}
todo = {}

class Hello(Resource): 
  
    def get(self): 
  
        return jsonify({'message': 'hello world'}) 
  
    def post(self): 
          
        data = request.get_json()     # status code 
        return jsonify({'data': data})
  
  
class Square(Resource): 
  
    def get(self, num): 
        print("In get sqauare method ")
        return jsonify({'square': num**2}) 


class TodoSimple(Resource):
    def post(self):
            data = request.get_json()
            return jsonify({'data':data})
    def get(self, todo_id):
        return {todo_id: todo[todo_id]}

    def put(self, todo_id):
        todo[todo_id] = request.form['data']
        return {todo_id: todo[todo_id]}
