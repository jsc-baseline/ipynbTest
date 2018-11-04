import random                                                           # imports proper libraries
class Company:                                                          # defines class name
    cotype = 'Generic'                                                  # type of company
    def __init__(self, name):                                           # constructor | inputs: self, name
        self.name = name                                                # sets name
        self.income = int(20000 + 80000 * random.random())              # sets income
        self.outgo = int(10000 + 50000 * random.random())               # sets outgo
        self.equity = int(500000 * random.random() ** 3)                # sets equity
    def __str__(self):                                                  # inputs: self
        return ("Name\t: %s\nIncome\t: %d\nOutgo\t: %d\nEquity\t: %d\n"
        % (self.name, self.income, self.outgo, self.equity))            # outputs: string
    def __add__(self, company2):                                        # inputs: self, company2
        company3 = Company('noname')                                    # sets name
        company3.income = self.income + company2.income                 # sets income
        company3.outgo = self.outgo + company2.outgo                    # sets outgo
        company3.equity = self.equity + company2.equity                 # sets equity
        return company3                                                 # outputs: company3
class CarCompany(Company):                                              # defines class name
    def __init__(self, ncars):                                          # constructor | inputs: self, ncars
        Company.__init__(self, 'Ford')                                  # extends to parent class
    def SetCars(self, ncars):                                           # inputs: self, ncars
        self.numberCars = ncars                                         # sets ncars
c1 = Company('ABC')                                                     # creates new company
c2 = Company('DEF')                                                     # creates new company
print(c1, c2)                                                           # prints companies
c3 = c1 + c2                                                            # adds companies
c3.name = 'XYZ'                                                         # sets name to company
print(c3)                                                               # print company
c1 = Company('ABC')                                                     # creates new company
print(c1.cotype)                                                        # sets type of company
c2 = Company('DEF')                                                     # creates new company
c1.cotype = 'Modern'                                                    # sets type of company
print(c1.cotype)                                                        # prints type of company
print(c2.cotype)                                                        # prints type of company
Company.cotype = 'Ultra Modern'                                         # sets type of company to parent class
print(c2.cotype)                                                        # prints type of company
print(c1.cotype)                                                        # prints type of company
c4 = CarCompany('Ford')                                                 # creates new car company
c4.SetCars(4)                                                           # sets number of cars to car company
print(c4.name, c4.numberCars)                                           # prints name and number of cars
c4 = CarCompany(4)                                                      # creates car company with number of cars
print(c4.name)                                                          # prints name of car company
c5 = CarCompany('Dodge')                                                # creates new car company
c5.SetCars(5)                                                           # sets number of cars to car company
print(c5.name, c5.numberCars)                                           # prints name and number of cars of company
c5 = CarCompany(5)                                                      # creates new car company
print(c5.name)                                                          # prints name of car company
