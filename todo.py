task = []

def add_task():
    task_input = input("\nEnter the task: ")
    task.append(task_input)
    print("\nYour task has been added!")
    
def view_task():
    list_num = 1
    print("\nThings to do: ")
    for item in task:
        print(f"{list_num}. {item}")
        list_num+=1

while True:
    print("\n*******Things To Do List*******")
    print("\n-------- Welcome to your To Do List --------\n")
    print("1. Add a task")
    print("2. View Tasks")
    print("3. Delete a task")
    print("4. Exit")
    
    user_input = input("\nEnter your choice(1-4): ")
    
    if user_input == "1":
        add_task()
    elif user_input == "2":
        view_task()
    elif user_input == "3":
        print("Not yet built")
    elif user_input == "4":
        print("See you again!")
        break
    else:
        print("Invalid input. Try again!")

#print(task)
