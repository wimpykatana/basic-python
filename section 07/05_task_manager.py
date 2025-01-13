import os

# File to store tasks
file_name = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split(" | ")
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks

# Save tasks to file   
def save_tasks(tasks):
    with open(file_name, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")

# Add a new task
def add_task(tasks):
    title = input("Enter the title of the task: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "Pending"}
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks
def view_task(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}]: {task['title']} - {task['status']}")

# Mark a task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter the task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "Complete"
        save_tasks(tasks)
        print(f"Task with id {task_id} marked as complete!")
    else: 
        print("Task not found!") 

# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter the task ID to delete: "))
    if task_id in tasks:
        del tasks[task_id]
        save_tasks(tasks)
        print(f"Task with id {task_id} deleted!")
    else:
        print("Task not found!")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()