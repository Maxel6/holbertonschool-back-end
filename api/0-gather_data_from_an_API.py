#!/usr/bin/python3

"""import request module"""
import requests


"""Define the base URL of the REST API"""
base_url = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(employee_id):
    try:
        """Make a GET request to fetch the employee's TODO list"""
        todo_url = f"{base_url}/todos?userId={employee_id}"
        response = requests.get(todo_url)

        """Check if the request was successful"""
        if response.status_code == 200:
            todos = response.json()

            """Get the user's name"""
            user_url = f"{base_url}/users/{employee_id}"
            user_response = requests.get(user_url)
            user_data = user_response.json()
            employee_name = user_data["name"]

            """Calculate TODO list progress"""
            total_tasks = len(todos)
            completed_tasks = [todo["title"]
                               for todo in todos if todo["completed"]]

            """Print the progress information"""
            print(f"Employee {employee_name} is done with tasks \
                  ({len(completed_tasks)}/{total_tasks}):")
            for task_title in completed_tasks:
                print(f"\t{task_title}")
        else:
            print(f"Error: Unable to fetch TODO list for \
                  Employee ID {employee_id}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    employee_id = int(input("Enter Employee ID: "))
    get_employee_todo_progress(employee_id)
