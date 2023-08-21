#!/usr/bin/python3
"""Python script that for a given employee ID returns all his todo list"""

import csv
import requests
import sys


if __name__ == "__main__":
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                         sys.argv[1], timeout=5)
    names = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1], timeout=5)

    json_todo = to_do.json()
    json_names = names.json()

    all_tasks = 0
    tasks_completed = 0

    titles_completed = []
    for task in json_todo:
        all_tasks += 1
        if task["completed"] is True:
            tasks_completed += 1
            titles_completed.append(task["title"])

    print('Employee {} is done with tasks({}/{}):'
          .format(json_names['name'], tasks_completed, all_tasks))

    for title_task in titles_completed:
        print('\t {}'.format(title_task))

    csv_filename = f"{sys.argv[1]}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for title_task in titles_completed:
            csv_writer.writerow(
                [sys.argv[1], json_names['name'], "Completed", title_task])
