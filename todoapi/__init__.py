from flask import Flask, jsonify, request
from mongoengine import connect
from Controllers.TodoController import TodoController
from flask_cors import CORS
import config

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# local DB
# connect('todos', host='127.0.0.1', port=27017)

isCloud = config.cloud_config
print(isCloud)

if isCloud is None or not isCloud:
    print('Taking default connection string')
    connect('todos', host='127.0.0.1', port=27017)
else:
    print('Taking cloud connection string')
    db_connection = config.cloud_db_connection
    connect(host=db_connection)


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
