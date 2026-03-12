import json
import os

class TODO():

    def add_todo(self):
        task = str(input("Fill this gap with task you wanna add:"))
        
        with open("todos.json", "r") as f:
            todos = json.load(f)
        
        new_task = {
            "id": len(todos) +1,
            "task": task,
            "status": True
        }

        todos.append(new_task)

        with open("todos.json", "w", encoding = "utf8") as f:
            json.dump(todos, f, indent = 4)

    def mark_as_done(self):
        with open("todos.json", "r") as f:
            todos = json.load(f)

        t_id = int(input("Enter task id:"))

        for todo in todos:
            if todo ["id"] == t_id:
                todo["status"] = True
        
        with open("todo.json", "w") as f:
            json.dump(todos, f, indent = 4)

    def print_todos(self):
        with open("todos.json", "r") as f:
            todos = json.load(f)
    
        for todo in todos:
            print(todo)


def init_file():
    if not os.path.exists("todos.json"):
        with open("todos.json", "w") as f:
            json.dump([], f)


def main():
    app = TODO()
    while True:
        print("There is your TODO list:")
        with open("todos.json") as f:
            todos = json.load(f)
        print("1.Check your todoes\n2.Add todo\n3.Mark todo as done")
        chs = int(input("Choose from num from list:"))
            
        if chs == 1:
            app.print_todos()
                
        elif chs == 2:
            app.add_todo()

        elif chs == 3:
            app.mark_as_done()


init_file()
main()