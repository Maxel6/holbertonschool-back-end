#!/usr/bin/python3

"""import request and sys module"""
import requests
import sys

if len(sys.argv) > 1:
    user_id = sys.argv[1]

    url_name = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    name_request = requests.get(url_name)
    todos_request = requests.get(url_todos)

    if name_request.status_code == 200:
        name_response = name_request.json()
        name = name_response["name"]

    if todos_request.status_code == 200:
        todos_response = todos_request.json()
        completed = []
        uncompleted = []
        for task in todos_response:
            if task['completed']:
                completed.append(task)
            else:
                uncompleted.append(task)
        todos_total = (len(completed) + len(uncompleted))

    output = "Employee {} is done with tasks({}/{}):".format(
        name, len(completed), todos_total)
    print(output)
    for task_name in completed:
        print(f"\t {task_name['title']}")
else:
    print("Please provide a user_id as a command-line argument.")