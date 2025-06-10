list_grade = []
list_name = []

# function for inputs
def display_student_summary():
    num_of_std = int(input("Enter the Number of Student:"))
    for i in range(num_of_std):
        name = input("Ente Student name:")
        list_name.append(name)
        grade = float(input("Enter Student Grade:"))
        if grade > 100 :
            print("Please Enter Correct Grade")
            grade = float(input("Enter Student Grade:"))
        list_grade.append(grade)
    print("Students Name :" , list_name ,"," , "Students Garde" , list_grade)