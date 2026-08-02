import logging
try:
    student1=int(input("Enter marks of student 1: "))
    student2=int(input("Enter marks of student 2: "))
    student3=int(input("Enter marks of student 3: "))
    student4=int(input("Enter marks of student 4: "))
    student5=int(input("Enter marks of student 5: "))

    if student1 >=80 and student1 <=75:
        print("Grade A")
    elif student2 >=75 and student2 <=60:
        print("Grade B")
    elif student3 >=60 and student3 <=50:
        print("Grade C")
    elif student4 >=50 and student4 <=40:
        print("Grade D")
    elif student5 >=40 and student5 <=30:
        print("Grade E")
    else:
        print("Grade F")
except ValueError:
    logging.error("Invalid input. Please enter numeric values for marks.")