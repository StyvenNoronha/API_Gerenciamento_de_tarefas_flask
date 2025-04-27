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
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "id nao encontrado"}), 404

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_tasks(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    if task == None:
        return jsonify({"message": "id nao encontrado"}), 404
    data = request.get_json()
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]
    return jsonify({"message": "tarefa atualizada com sucesso"})

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = None  
    for t in tasks:
        if t.id == id:
            task = t
            break 

    if task is None:
        return jsonify({"message": "id nao encontrado"}), 404

    tasks.remove(task)
    return jsonify({"message": "tarefa removida com sucesso"})

                    


if __name__ == "__main__":
    app.run(debug=True)
