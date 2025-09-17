import json
import os
'''
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

Add, Update, and Delete tasks

Mark a task as in progress or done

List all tasks

List all tasks that are done

List all tasks that are not done

List all tasks that are in progress

Here are some constraints to guide the implementation:

You can use any programming language to build this project.

Use positional arguments in command line to accept user inputs.

Use a JSON file to store the tasks in the current directory.

The JSON file should be created if it does not exist.

Use the native file system module of your programming language to interact with the JSON file.

Do not use any external libraries or frameworks to build this project.

Ensure to handle errors and edge cases gracefully.
'''

filename = "data.json"
if os.path.exists(filename):
    with open("data.json","r") as file:
        task_list = json.load(file)
else:
    task_list = {}

def add_task(task_name, task_status = None):
    if task_status == "in progress" or task_status == "done":
        task_list[task_name] = task_status
    else:
        task_list[task_name] = None
        return print("Task created; task status currently unknown. Use in progress or done")

def update_task(task_name, task_status):
    if task_status == None:
        return print("task status not defined")
    if task_name not in task_list:
        return print("task does not exist in task list")
    task_list[task_name] = task_status

def delete_task(task_name):
    if task_name in task_list:
        task_list.pop(task_name)


while True:
    option_input = input("Add, Update, or Delete? Or List Tasks (or Quit)")

    if option_input == "Quit":
        break

    if option_input in ["Add","Update"]:
        task_name = input("Task name?")
        option_status = input("Task status? in progress or done")
        if option_input == "Add":
            add_task(task_name,option_status)
        elif option_input == "Update":
            update_task(task_name,option_status)
    elif option_input in ["Delete"]:
        task_name = input("Which Task to delete?")
        delete_task(task_name)
        print(f"Task {task_name} deleted")
    elif option_input == "List Tasks":
        task_input = input("All, Done, or In Progress?")
        if task_input.lower() == "all":
            print(task_list)
        elif task_input.lower() == "done":
            for key, value in task_list.items():
                if value.lower() == "done":
                    print(key, ":", value)
        elif task_input.lower() == "in progress":
            for key, value in task_list.items():
                if value.lower() == "in progress":
                    print(key, ":", value)

with open("data.json", "w") as file:
    json.dump(task_list, file, indent=4)

#This is not CLI. Will need to refactor this.

# def main():
#     x = 0
#
# if __name__ == "__main__":
#     main()
#     print("main!")


