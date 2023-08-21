#!/usr/bin/python3
"""Python script that for a given employee ID returns all his todo list and exports it to CSV"""

import csv
import requests
import sys


if __name__ == "__main__":
    to_do = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1], timeout=5)
    names = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + sys.argv[1], timeout=5)

    json_todo = to_do.json()
    json_names = names.json()

    print(json_names)

    all_tasks = 0
    task_data = []

    for task in json_todo:
        all_tasks += 1
        task_title = task["title"]
        task_completed = "True" if task["completed"] else "False"
        task_data.append([sys.argv[1], json_names['username'],
                         task_completed, task_title])

    csv_filename = f"{sys.argv[1]}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(task_data)
