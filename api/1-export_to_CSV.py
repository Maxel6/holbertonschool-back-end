#!/usr/bin/python3
"""Python script that for a given employee ID returns all his todo list and exports it to CSV"""

import requests
import sys
import csv

if __name__ == "__main__":
    # Make API requests to fetch data
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1], timeout=5)
    names = requests.get('https://jsonplaceholder.typicode.com/users/' + sys.argv[1], timeout=5)

    # Parse JSON responses
    json_todo = to_do.json()
    json_names = names.json()

    # Initialize variables to count tasks and store their titles and completion status
    all_tasks = 0
    task_data = []

    # Iterate through tasks and collect data
    for task in json_todo:
        all_tasks += 1
        task_title = task["title"]
        task_completed = "True" if task["completed"] else "False"
        task_data.append([sys.argv[1], json_names['name'], task_completed, task_title])

    # Export data to CSV
    csv_filename = f"{sys.argv[1]}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)  # Specify quoting option
        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        # Write data for each task
        csv_writer.writerows(task_data)

