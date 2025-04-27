from flask import Flask, request, jsonify  # type: ignore
from models.task import Task

app = Flask(__name__)

tasks = []
tasksIdControl = 1

@app.route("/tasks", methods=["POST"])
def create_tasks():
    global tasksIdControl
    data = request.get_json()
    new_task = Task(id=tasksIdControl, title=data.get("title"), description=data.get("description", " "))
    tasksIdControl += 1
    tasks.append(new_task)
    return  jsonify({"message":"Nova tarefa criada com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
