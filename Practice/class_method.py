""" 
Instance methods = Best for operations on instance of the class (objects)
Static methods = Best for utility functions that do not need access to class data
Class methods = Best for class-level data or require access to the class itself

"""

class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa) -> None:
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    # Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return (cls.total_gpa/cls.count)
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    
student1 = Student("Mark", 3.4)
student2 = Student("John", 4)
print(student1.get_info())
print(Student.get_count())
print("Avarage gpa: ", Student.avg_gpa())