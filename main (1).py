# i hate lists and funcations.


tasks = []

#apppreantly im adding a funcation bec my code wouldnt works otherwise
def add_task (task, tasks):
    tasks.append(task)

while True:
    print("To Do List")
    print("View Tasks - 1")
    print("Add Tasks - 2")
    print("To Leave menu - 3")
    
    
    number = int(input("Enter your number (1-3): "))
    
    if number == 1:
        print("Your Tasks: ")
        for task in tasks:
            print("-" + task)
    
    
    elif number == 2:
        new_task = input("Enter your new task: ")
        add_task(new_task, tasks)
     
        
    
    elif number == 3:
        print("Bye")
        break
    
    else:
        print("\ninvalid number please choose a number from 1 to 3")
    
    
    

    
