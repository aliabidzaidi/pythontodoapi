from flask import Flask, jsonify, request
from mongoengine import connect
from Controllers.TodoController import TodoController
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# local DB
# connect('todos', host='127.0.0.1', port=27017)

isCloud = os.environ.get('IS_CLOUD', None)
print(isCloud)

if isCloud is None or isCloud != 'TRUE':
    print('Taking default connection string')
    connect('todos', host='127.0.0.1', port=27017)

else:
    print('Taking cloud connection string')
    db_connection = os.environ.get('MONGODB_URL', None)
    connect(host=db_connection)


@app.route("/", methods=['GET'])
def index():
    return jsonify(message="Api works.."), 200


@app.route("/todos", methods=['GET'])
def todos():
    obj = TodoController()
    return obj.getTodos()


@app.route("/todo/<id>", methods=['GET'])
def get_todo(id):
    obj = TodoController()
    print(id)
    return obj.getTodo(id)


@app.route("/todos/add", methods=['POST'])
def add_todo():
    obj = TodoController()
    return obj.addTodo()


@app.route("/todo/<id>", methods=['PUT'])
def edit_todo(id):
    obj = TodoController()
    return obj.editTodo(id)


@app.route("/todo/<id>", methods=['DELETE'])
def delete_todo(id):
    obj = TodoController()
    return obj.deleteTodo(id)