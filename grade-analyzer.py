

# function for inputs
def display_student_summary():
    num_of_std = int(input("Enter the Number of Student:"))
    for i in range(num_of_std):
        name = input("Ente Student name:")
        list_name.append(name)
        grade = float(input("Enter Student Grade:"))
        while grade > 100 :
            print("Please Enter Correct Grade")
            grade = float(input("Enter Student Grade:"))
        list_grade.append(grade)
    print("Students Name :" , list_name ,"," , "Students Garde" , list_grade)


     # function to get average
def get_avg_grade():
        avg = sum(list_grade) / len(list_grade)
        print("Te Average Of Grades Is :",avg )
        return avg 


   # function to get the highest grade
def get_heighest_grade():
    highest = max(list_grade)  # Find the highest grade
    h_grade = highest
    n_grade = []

    # Loop through the list to find all students with the highest grade
    for i, grade in enumerate(list_grade):
        if grade == highest:
            n_grade.append(list_name[i])

    print("The highest grade is:", h_grade)
    print("The name(s) of the student(s) with the highest grade:", n_grade)



# function to count the number of the student passed
def count_passed(list_grade):
    count = 0
    for i in  range(len(list_grade)) :
        if list_grade[i] >= 65:
          count +=1
    print("the number of students passed is :" , count)
    return count
list_grade = []
list_name = []
display_student_summary()
get_avg_grade()
get_heighest_grade()
count_passed(list_grade)

    