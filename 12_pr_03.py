# salaryAfterIncrement =  salary * increment

class Employee:
    salary = 15000
    increment = 2.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 20000
print(e.increment)
