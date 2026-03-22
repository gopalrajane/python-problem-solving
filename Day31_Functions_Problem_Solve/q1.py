# Q. Mini Project: Student Record System

Students = {

}


def add_student(N):
    for i in range(N):
        name = input("Name : ")
        marks = int(input("Marks :"))
        Students[name] = marks
    
    return Students
    

def display_Student(Students):
    print('\nAll Students : ')
    for keys, values in Students.items():
        print(f'{keys} : {values}')


def find_topper(Students):
    topper_marks = 0
    for keys,values in Students.items():
        if values > topper_marks:
            topper_marks = values
            toppper_student = keys
    
    print(f'\nTopper Student : {toppper_student} ,({topper_marks})\n')


def search_student(search_name, Students):
    
    if search_name in Students:
        print(f"Marks : {Students[search_name]}")
    else:
        print("Student not Found.")
            


# Optional Code
while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Find Topper")
    print("4. Search Student")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        N = int(input("How many students: "))
        add_student(N)

    elif choice == 2:
        display_Student(Students)

    elif choice == 3:
        find_topper(Students)

    elif choice == 4:
        name = input("Enter name: ")
        search_student(name, Students)

    elif choice == 5:
        break 
    




