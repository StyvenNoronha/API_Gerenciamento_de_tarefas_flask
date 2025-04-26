from flask import Flask, request # type: ignore
from models.task import Task
app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def create_tasks():
    data = request.get_json()

    return data



if __name__ == "__main__":
    app.run(debug=True)
