class ToDoList:
    def __init__(self):
        self.tasks = {}

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for task_id, task in self.tasks.items():
                print(f"{task_id}: {task}")

    def add_task(self, task):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = task
        print(f"Task added: {task}")

    def update_task(self, task_id, new_task):
        if task_id in self.tasks:
            self.tasks[task_id] = new_task
            print(f"Task {task_id} updated to: {new_task}")
        else:
            print(f"Task {task_id} not found.")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            removed_task = self.tasks.pop(task_id)
            print(f"Task {task_id}: {removed_task} removed.")
        else:
            print(f"Task {task_id} not found.")

# Example usage
todo_list = ToDoList()

while True:
    print("\nOptions:")
    print("1. Display tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Remove task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        todo_list.display_tasks()
    elif choice == "2":
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == "3":
        task_id = int(input("Enter the task ID to update: "))
        new_task = input("Enter the new task: ")
        todo_list.update_task(task_id, new_task)
    elif choice == "4":
        task_id = int(input("Enter the task ID to remove: "))
        todo_list.remove_task(task_id)
    elif choice == "5":
        print("Exiting the to-do list program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
