#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      chyas
#
# Created:     31/01/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def task():
    tasks=[]
    print("------Welcome to Task Management System")

    total_task=int(input("Enter Number How many task You want to add:\n"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter Task {i}=")
        tasks.append(task_name)

    print(f"Todays Tasks are \n {tasks}")

    while True:
        op =int(input("Enter \n 1-Add \n 2-Update \n 3-Delete \n 4-View \n 5-Exit"))
        if op == 1:
            add=input("Enter a Task U want to add:\n")
            tasks.append(add)
            print(f"Task {add} has been added...........................")

        elif op == 2:
            update_val =input("Enter the Task name you want to update:\n")
            if update_val in tasks:
                up = input("Enter new task:\n")
                ind= tasks.index(update_val)
                tasks[ind]=up
                print(f"Task {up} Updated..............................")

        elif op == 3:
            del_val =input("Enter task you want to delete:")
            if del_val in tasks:
                ind= tasks.index(del_val)
                del tasks[ind]
                print("Task {del_val} Deleted successfully......")


        elif op==4:
           print(f"total_task = {tasks}")

        elif op ==5:
           print("System Closing...------------------....")
           exit()

        else:
            print("Invalid choice......")

task()
