from flask import Flask, request, jsonify  # type: ignore
from models.task import Task

app = Flask(__name__)

tasks = []
tasksIdControl = 1


@app.route("/tasks", methods=["POST"])
def create_tasks():
    global tasksIdControl
    data = request.get_json()
    new_task = Task(
        id=tasksIdControl,
        title=data.get("title"),
        description=data.get("description", " "),
    )
    tasksIdControl += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso"})


@app.route("/tasks", methods=["GET"])
def read_tasks():
    taskList = [task.to_dict() for task in tasks]
    output = {"tasks": taskList, "total_tasks": len(taskList)}

    return jsonify(output)

@app.route("/tasks/<int:id>", methods=["GET"])
def read_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message":"id nao encontrado"}), 404    


if __name__ == "__main__":
    app.run(debug=True)
