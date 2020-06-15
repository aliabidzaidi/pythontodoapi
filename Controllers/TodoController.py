from flask import jsonify, request
from Models.Todo import Todo
import datetime
import bson


class TodoController:

    def getTodos(self):
        try:
            page = int(request.args.get('page', default=1))
            limit = int(request.args.get('limit', default=8))
            skip = (page - 1)*limit

            # Todo.objects returns of mongodb
            # It is not a python dictionary
            # mongoDB [<Todo>, <Todo>, <Todo>] -> python list of dictionaries [ {Todo}, {Todo}, {Todo}]
            todos = Todo.objects(isDeleted=False).skip(skip).limit(limit)
            todoCount = Todo.objects(isDeleted=False).count()
            todoList = []
            for todo in todos:
                todoList.append(todo.asdict())
            return jsonify(data=todoList, count=todoCount), 200
        except Exception as ex:
            print('exception occurrrrrred! look: ', ex)
            return jsonify(message="An error occurred"), 500

    def getTodo(self, todoId):
        try:
            isValidId = bson.objectid.ObjectId.is_valid(todoId)
            if not isValidId:
                return jsonify(message="Invalid data submitted"), 400

            todo = Todo.objects(id=todoId).first()

            if not todo:
                return jsonify(message="Todo doesn't exist"), 400

            return jsonify(data=todo.asdict()), 200

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

    def editTodo(self, todoId):
        try:
            data = request.get_json()
            isValidId = bson.objectid.ObjectId.is_valid(todoId)
            if not data["heading"] or not data["body"] or not isValidId:
                return jsonify(message="Invalid data submitted"), 400

            heading = data["heading"]
            body = data["body"]
            colorCode = data["colorCode"]

            todo = Todo.objects(id=todoId).first()
            if not todo:
                return jsonify(message="Todo not found"), 400

            todo.heading = heading
            todo.body = body
            todo.colorCode = colorCode
            todo.dateUpdated = datetime.datetime.now()
            todo.save()
            return jsonify(message='Todo updated successfully', data=todo.asdict())

        except Exception as ex:
            return jsonify(message="An error occurred", error=ex.message), 500

    def deleteTodo(self, todoId):
        try:

            isValidId = bson.objectid.ObjectId.is_valid(todoId)
            if not isValidId:
                return jsonify(message="Invalid data submitted"), 400

            todo = Todo.objects(id=todoId).first()
            if not todo:
                return jsonify(message="Todo not found"), 400

            todo.dateUpdated = datetime.datetime.now()
            todo.isDeleted = True
            todo.save()
            return jsonify(message='Todo deleted successfully'), 200

        except Exception as ex:
            return jsonify(message="An error occurred", error=ex.message), 500
