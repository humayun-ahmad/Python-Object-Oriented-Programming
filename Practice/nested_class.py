# Nested class 

class Company:
    class Employee:
        def __init__(self, name, position) -> None:
            self.name = name
            self.position = position
            
        def get_details(self):
            return f"{self.name} {self.position}"
    
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.employees = []
        
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
    
    def list_employees(self):
        return [employee.get_details() for employee in self.employees]
    

company = Company("Krusty Krab")

# print(company.company_name)
company.add_employee("Eugene", "Manager")
company.add_employee("Spongebob", "Cook")
company.add_employee("Squidward", "Cashier")

print(company.list_employees())



