import os       # import functon for clear screen
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def calculator():
    num1=float(input("enter a first number="))
    operation_dict={'+':add,'-':sub,'*':mul,'/':div}
    for symbol in operation_dict.keys():
        print(symbol)
    flip=True    
    while flip:    
        op_symbol=input("peak an operaation=")
        num2=float(input("enter next number="))
        calculating_function=operation_dict[op_symbol] 
        output=calculating_function(num1,num2)   
        print(f"{num1} {op_symbol} {num2}={output}")
        continue_cal=input(f"enter 'y' for continue calculation with {output},'n' for new calculation and 'x' for exit=").lower()
        if(continue_cal=='y'):
            num1=output
        elif continue_cal=='n':
            os.system("cls")        # used for clear the screen
            calculator()        #recursion
        else:
            flip=False
            print("BUY....")
calculator()







