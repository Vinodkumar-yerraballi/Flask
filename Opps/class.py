class Employee:
    num_of_employee=0
    raise_amount=1.05
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' +last +'@company.com'
        Employee.num_of_employee +=1
    def amount_rise(self):
        self.pay= int(self.pay * self.raise_amount)

    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    def promotions(self):
        if self.pay > 50000:
            return "Promoted"
        else:
            return "Not Promoted"
    @classmethod
    def class_method(cls,amount):
        cls.pay=amount
    





emp_1=Employee('Vinod','Kumar',5000)
emp_2=Employee('Jack','Tailor',7000)
Employee.raise_amount
Employee.promotions
Employee.amount_rise
Employee.full_name
Employee.raise_amount
Employee.promotions
# print(emp_1.first)
# print(emp_2.pay)
# print(emp_1.email)
# emp_1.full_name
print(emp_1.full_name())
# print(emp_1.raise_amount())
print(emp_1.amount_rise())
# print(Employee.amount_rise)
# print(emp_1.num_of_employee)
# Employee.raise_amount=1.5
# print(emp_1.raise_amount) 
print(emp_2.promotions())
Employee.class_method
print(emp_1.class_method(200))
