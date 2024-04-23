# - Write a OOP in python to input empid, name, basic salary, no. of experience in yrs. Calculate hra(35% of basic), da (58% of basic) and pf (9.5% of basic).
# Also calculate bonus based on experience in years.
# If experience in years is >= 30, bonus must be 59% of basic, If experience in years is >=23, 
# bonus must be 51% of basic, If experience in years is >=15, bonus must be 45% of basic, 
# If experience in years is >=7, bonus must be 33% of basic, If experience in years is <7, 
# bonus must be 16% of basic Calculate netsalary as basic+da+hra-pf+bonus.
# Create a class, constructor to create instance variables, getter-setter for each variable, calculative functions for operative variables. A class methods/function should not contain
# display specific and input specific code. Such code should be added in driver part of python program.

class Employee:
    def __init__(self, empid:int, name:str, baseSalary:float, experience:int):
        self.empid = empid
        self.name = name
        self.bSalary = baseSalary
        self.experience = experience
    
    def calc_HRA(self):
        self.hra = (35/100)*self.bSalary
        return self.hra
    
    def calc_DA(self):
        self.da = (58/100)*self.bSalary
        return self.da
    
    def calc_PF(self):
        self.pf = (9.5/100)*self.bSalary

    def calc_BONUS(self):
        if self.experience >= 33:
            self.bonus = (59/100)*self.bSalary
        elif self.experience >= 23:
            self.bonus = (51/100)*self.bSalary
        elif self.experience >= 15:
            self.bonus = (45/100)*self.bSalary
        elif self.experience >= 7:
            self.bonus = (33/100)*self.bSalary
        else:
            self.bonus = (16/100)*self.bSalary
        return self.bonus
    
    def calc_NET(self):
        self.calc_HRA()
        self.calc_DA()
        self.calc_PF()
        self.calc_BONUS()

        self.netsalary = self.bSalary + self.da + self.hra - self.pf + self.bonus
        
        return self.netsalary

a = Employee(
    int(input("Emp ID: ")),
    input("Name: "),
    float(input("Base Salary: ")),
    int(input("Experience: "))
)

print(a.calc_NET())