

class Student_management():
    pass





def main_menu():
    print("Select an option:")
    print("1: Student Management")
    print("2: Teacher Management")
    print("3: Exit")


def student_menu():
    print("Student Management Options:")
    print("1: Add Student")    
    print("2: View Student Details")    
    print("3: Update Student Details")    
    print("4: Remove Student")

def teacher_menu():
    print("Teacher Management Options:") 
    print("1: Add Teacher") 
    print("2: View Teacher Details") 
    print("3: Update Teacher Details") 
    print("4: Remove Teacher") 



def start_program():
    
    while True:
        main_menu()
        choice = input("Enter your choice (1-3)")
        
        if choice == "1":
            student_menu()
            student_choice = input("Enter your choice for Student Management : ")
            handle_student(student_choice)
            
        elif choice == "2":
            teacher_menu()
            teacher_choice = input("Enter your choice for Teacher Management : ")
            handle_teacher(teacher_choice)
            
            


def handle_student(choice):
    print(f"your choice is {choice}")


def handle_teacher(choice):
    print(f"your choice is {choice}")
    
    
    
    
    
start_program()