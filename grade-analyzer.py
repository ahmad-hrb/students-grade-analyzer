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

     # function to get average
    def get_avg_grade():
        avg = sum(list_grade) / len(list_grade)
        print("Te Average Of Grades Is :",avg )
        return avg 
    get_avg_grade()
    
      # function to get the highest grade
    def get_heighest_grade():
        greater_grd = list_grade[0]
        num = 0
        for i , ele in enumerate(list_grade):
            
            if ele > greater_grd :
                greater_grd = ele
                num = i
        print("the highest grade is :" , greater_grd)
        print("the name of the student have highest grade is :" , list_name[num])
    get_heighest_grade()
display_student_summary()

    