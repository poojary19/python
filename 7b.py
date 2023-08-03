class employee:
    def __init__(self):
        self.name=""
        self.id=""
        self.salary=""
        self.dept=""

    def getempdetails(self):
        self.name = (input("enter the name of the employee"))
        self.id = (input("enter the id of the employee"))
        self.salary = (input("enter the salary of the employee"))
        self.dept = (input("enter the department of the employee"))

    def showempdetails(self):
        print("employee details")
        print("name:",self.name)
        print("id:",self.id)
        print("salary:",self.salary)
        print("dept:",self.dept)
    def updtsalary(self):
        self.salary=int(input("enter new salary"))
        print("update salary",self.salary)

e1=employee()
e1.getempdetails()
e1.showempdetails()
e1.updtsalary()

