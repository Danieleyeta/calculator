def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2


operations= {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    
    }

def my_calculator(): 
    continue_calculator= True
    
    first_num=float(input("input your first number: "))
    
    while continue_calculator:
        operator= input("pick a mathematical operator '+', '-', '*', '/': ")
        second_num= float(input("input second number: "))
        result = operations[operator](first_num,second_num)
        print(f"{first_num} {operator} {second_num} = {result}")
        proceed=input(f"Do you want to continue with the {result}? if yes type y, if no type n:  ").lower()
        if proceed == "y":
            first_num =result
        elif proceed == "n":
            continue_calculator= False
            my_calculator()
        else:
            print("wrong, you should have inputted a y or n")
            
            
my_calculator()
            