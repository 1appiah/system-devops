#!/usr/bin/python3
"""gather data from an API"""
import csv
import json
import requests

emp_info = 'https://jsonplaceholder.typicode.com/users/'
all_todos = 'https://jsonplaceholder.typicode.com/todos'
if __name__ == "__main__":
    get_emp_info = json.loads(requests.get(emp_info).text)
    get_all_todos = json.loads(requests.get(all_todos).text)
    todos_done_list = []
    name = None

    to_js = dict()
    todos = []
    for user in get_emp_info:
        for i in get_all_todos:
            if user['id'] == i['userId']:
                this_info = {"task": i['title'], "completed": i['completed'],
                             "username": user['username']}
                todos.append(this_info)
        to_js[user['id']] = todos
        todos = []
    with open("todo_all_employees.json", "w", encoding="utf8") as f:
        f.write(json.dumps(to_js))
