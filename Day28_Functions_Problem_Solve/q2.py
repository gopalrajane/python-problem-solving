# Q. Student Report Card

def calculate_total(marks):
    total = 0
    for m in marks:
        total += m
    return total


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def find_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'Fail'


def generate_report(students):

    print("\nStudent Report Card:\n")

    for name, marks in students.items():

        total = calculate_total(marks)
        avg = calculate_average(marks)
        grade = find_grade(avg)

        print(f"{name} -> Total: {total}, Avg: {avg:.2f}, Grade: {grade}")



students = {}

N = int(input("Enter number of students: "))

for _ in range(N):
    name = input("Enter Name: ")
    marks = []

    for _ in range(3):
        marks.append(int(input("Marks: ")))

    students[name] = marks


generate_report(students)


