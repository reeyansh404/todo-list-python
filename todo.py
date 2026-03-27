task = []

def add_task():
    task_input = input("\nEnter the task: ")
    task.append(task_input)
    print("\nYour task has been added!")
    
def view_task():
    list_num = 1
    for item in task:
        print("\nThings to do: ")
        print(f"{list_num}. {item}")
        list_num+=1
    else:
        print("\nThere are no task to be completed.")
        
def delete_task():
    view_task()
    del_task = int(input("\nEnter the task you want to delete in number: "))
    del_task -=1 #trying to fit the index
    
    try:
        index = del_task
        del_items = task.pop(index)
        print(f"The item you selected {del_task+1} is now deleted.")
    except ValueError:
        print("Invalid input! Please enter a valid integer") #not fixed yet 
    except IndexError:
        print("Value not on the list!")
    

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
        delete_task()
    elif user_input == "4":
        print("See you again!")
        break
    else:
        print("Invalid input. Try again!")
