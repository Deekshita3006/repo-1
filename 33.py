#project Calculator.

def add (n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operation={"+": add,
            "-":subtract,
            "*":multiply,
            "/":divide}
def caluclator():
 
 should_accumlate=True
 n1=float(input("what is your first number? "))
 while should_accumlate:



    for symbol in operation:
      print(symbol)
    operation_symbol=input("pick your operation: ")
    n2=float(input("what is your second number? "))

    answer=operation[operation_symbol](n1,n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")
    choice=input(f"type 'yes' to continue calculating with {answer} .type 'n' for new calculation ")
    if choice=="yes":
     n1=answer
    else:
     should_accumlate=False
     print("\n"*10)
     caluclator()
     
caluclator()




