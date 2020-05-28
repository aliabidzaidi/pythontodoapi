from flask import jsonify, request
from Models.Todo import Todo

class TodoController:

    def getTodos(self):
        try:
            page = int(request.args.get('page', default=1))
            limit = int(request.args.get('limit', default=8))
            skip = (page -1)*limit


            # Todo.objects returns of mongodb
            # It is not a python dictionary 
            # mongoDB [<Todo>, <Todo>, <Todo>] -> python list of dictionaries [ {Todo}, {Todo}, {Todo}]
            todos = Todo.objects().skip(skip).limit(limit)
            todoCount = Todo.objects().count()
            todoList = []
            for todo in todos:
                todoList.append(todo.asdict())
            return jsonify(data=todoList, count=todoCount), 200
        except Exception as ex:
            print('exception occurrrrrred! look: ', ex)
            return jsonify(message="An error occurred"), 500
        

    def addTodo(self):
        try:
            data = request.get_json()
            if not data["heading"] or not data["body"]:
                return jsonify(message="Invalid data submitted"), 400 

            print(data)
            heading = data["heading"]
            body = data["body"]
            colorCode = data["colorCode"]

            todo = Todo(heading=heading, body=body, colorCode=colorCode)

            todo.save()
            return jsonify(message='Todo added successfully')
        
        except Exception as ex:
            return jsonify(message="An error occurred", error=ex.message), 500