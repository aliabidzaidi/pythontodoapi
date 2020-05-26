from flask import Flask, jsonify, request
from mongoengine import connect
from Controllers.TodoController import TodoController
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

connect('todos', host='127.0.0.1', port=27017)


@app.route("/", methods=['GET'])
def index():
    return "api works.."


@app.route("/todos", methods=['GET'])
def todos():
    obj = TodoController()
    return obj.getTodos()


@app.route("/todos/add", methods=['POST'])
def add_todo():
    obj = TodoController()
    return obj.addTodo()
