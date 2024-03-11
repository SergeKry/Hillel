class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @staticmethod
    def from_string(string):
        data = string.split("-")
        first_name = data[0]
        last_name = data[1]
        salary = int(data[2])
        return Employee(first_name, last_name, salary)

emp2 = Employee.from_string('John-Smith-55000')
print(emp2.first_name, emp2.last_name, emp2.salary)