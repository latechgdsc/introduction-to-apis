from flask import Flask
from flask_restful import Api, Resource, reqparse, abort


# this allows flask to find the right files and libraries
app = Flask(__name__)
api = Api(app)

# to do list
todos = {
    '1': {'task': 'build an API'},
    '2': {'task': '?????'},
    '3': {'task': 'profit!'},
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in todos:
        abort(404, message=f"Todo {todo_id} doesn't exist")

parser = reqparse.RequestParser()
parser.add_argument('task')


class Todo(Resource):
    
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return {todo_id: todos[todo_id]}, 200

    def post(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        todos[todo_id] = task
        return task, 201

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del todos[todo_id]
        return '', 204

    def put(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        args = parser.parse_args()
        task = {'task': args['task']}
        todos[todo_id] = task
        return task, 201



# this is a list of apis for the todolist
class Todolist(Resource):

    def get(self):
        return todos, 200

    def delete(self):
        todos.clear()
        return '', 204


# add the classes to the api method
api.add_resource(Todo, '/todo/<string:todo_id>') # www.coolwebiste.com/todo/1
api.add_resource(Todolist, '/todolist')


if __name__ == '__main__':
    app.run(debug=True)