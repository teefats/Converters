class Calculator:
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b =b
        
    def multiplication(self):
        # return self.a * self.b
        print(a *b)
    
    def addition(self):
        # return self.a + self.b
        print(a +b)
    def subtraction(self):
        # return self.a  - self.b
        print(a - b)
    def division(self):
        # return self.a / self.b
        print(a / b)

a = int(input("Please enter a number"))
b = int(input("Please eneter a number"))      


obj =Calculator()

history = []
def calc():
    try:
        # a = int(input("Please enter a number"))
        # b =int(input("Please eneter a number"))   
        running = True
        while running != False:
            
            operation_type =input("Please enter the type of operation you would like, The options are Multiplication, Addition, Subtraction, Division").lower()
           
            if operation_type == "multiplication":
                result = obj.multiplication()
                
            elif operation_type == "addition":
                result = obj.addition()
            elif operation_type == "subtraction":
                result = obj.subtraction()
            elif operation_type == "division":
                result = obj.division()
            else:
                print("Please enter a valid operation")
        history.append(result)
        choice = input("Do you want to continue? Yes or No")
        if choice == "Yes":
            running = True
        else:
            running = False
        
        
    except ValueError:
        print("Please enter a valid number")
    history_choice = input("Do you want to see your history? Yes or No")
    if history_choice == "Yes":
        print(history)

calc()


