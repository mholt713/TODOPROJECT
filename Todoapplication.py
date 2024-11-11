tasks = []

def add_task():
    task = input("What do you need to add?")
    tasks.append(task)
    print("Your task has been added to your list")
    
def view_tasks():
    if len(tasks) == 0:
        print("You currently have no tasks to complete.")
    else: 
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def delete_task():
    if len(tasks) == 0:
        print("You currently have no tasks to delete.")
    else:
        print("tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        choice = int(input("Please enter the number of the task you want to delete: "))
        if 0 < choice <= len(tasks):
            del tasks[choice - 1]
            print("Task deleted successfully.")
        else:
            print("Task does not exist")

def main():
        while True:
            try:
                print("\nHello, welcome to your to do list.")
                print("""What would you like to do?
        1. ADD TASKS    2. VIEW TASKS
        3. DELETE TASKS 4. QUIT APP""")
                choice = int(input("Please select an option on the screen: "))
                if choice == 1:
                    add_task()
                elif choice == 2:
                    view_tasks()
                elif choice == 3:
                    delete_task()
                elif choice == 4:
                    print("Thank you for using YOUR TO DO LIST")
                    break        
                else: 
                    print("That is not an option. Please try again.")
            except ValueError:
                print("Please enter one of the numerical options present.")
            

if __name__ == "__main__":
    main()
