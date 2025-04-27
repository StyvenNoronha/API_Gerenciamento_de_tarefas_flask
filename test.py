import pytest 
import requests

BASE_URL ='http://127.0.0.1:5000'
tasks = []

def testCreateTasks():
    testCreate = {
        "title":"title test",
        "description":"description test"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=testCreate)

    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def testGetTasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def testGetTask():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']


