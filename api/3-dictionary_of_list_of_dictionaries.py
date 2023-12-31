#!/usr/bin/python3
"""Python script that fetches and
exports all tasks from all employees in JSON format"""

import json
import requests


def fetch_employee_data(employee_id):
    to_do = requests.get(f'https://jsonplaceholder.typicode\
.com/todos?userId={employee_id}', timeout=5)
    names = requests.get(f'https://jsonplaceholder.typicode.\
com/users/{employee_id}', timeout=5)

    if to_do.status_code == 200 and names.status_code == 200:
        json_todo = to_do.json()
        json_names = names.json()

        task_data = {
            "username": json_names['username'],
            "tasks": [
                {
                    "task": task["title"],
                    "completed": task["completed"]
                }
                for task in json_todo
            ]
        }

        return task_data

    return None


if __name__ == "__main__":
    all_employee_data = {}

    for employee_id in range(1, 11):
        employee_data = fetch_employee_data(employee_id)
        if employee_data:
            user_id = str(employee_id)
            if user_id not in all_employee_data:
                all_employee_data[user_id] = []
            all_employee_data[user_id].append(employee_data)

    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_employee_data, json_file)
