#!/usr/bin/python3
"""gather data from an API"""
import json
import requests
from sys import argv

emp_info = 'https://jsonplaceholder.typicode.com/users'
all_todos = 'https://jsonplaceholder.typicode.com/todos'
if __name__ == "__main__":
    emp_id = argv[1]
    get_emp_info = requests.get(emp_info).json()
    get_all_todos = requests.get(all_todos).json()
    to_dos = 0
    todos_done = 0
    todos_done_list = []
    name = None
    for i in get_emp_info:
        if i['id'] == int(emp_id):
            name = i['name']
    for item in get_all_todos:
        if item['userId'] == int(emp_id):
            to_dos += 1
            if item["completed"]:
                todos_done_list.append(item["title"])
                todos_done += 1
    print("Employee {} is done with tasks({}/{}):\n"
          .format(name, todos_done, to_dos), end="")
    for item in todos_done_list:
        print("\t {}\n".format(item), end="")
