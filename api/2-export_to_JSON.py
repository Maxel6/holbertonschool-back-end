#!/usr/bin/python3
"""Python script that for a given employee ID
returns all his todo list and exports it to JSON"""

import json
import requests
import sys


if __name__ == "__main__":
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId='
                         + sys.argv[1], timeout=5)
    names = requests.get('https://jsonplaceholder.typicode.com/users/'
                         + sys.argv[1], timeout=5)

    json_todo = to_do.json()
    json_names = names.json()

    task_data = {
        sys.argv[1]: [
            {
                "username": json_names['username'],
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in json_todo
        ]
    }
    print (task_data)

    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(task_data, json_file)
