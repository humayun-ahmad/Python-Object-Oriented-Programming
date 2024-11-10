
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    def display(self,text):
        return f"{text} am talking form display!"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions



print(Employee.is_valid_position("Manager1"))
print(Employee.display("","Eugune"))
employee1 = Employee("Mark", "Manager")
employee2 = Employee("Miller", "Cashier")

print(employee1.get_info())
print(employee1.is_valid_position("Cook"))


