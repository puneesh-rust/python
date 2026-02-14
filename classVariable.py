class Student:
    Passout_Year =2025
    student_Count =0

    def __init__(self,name,age,location):
        self.name = name
        self.age = age 
        self.location = location

        Student.student_Count += 1
std1 = Student("puneesh",22,"agra")
std2= Student("raj",23,"goa")     

print(Student.student_Count)
