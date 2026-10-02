
def sequential_calculator():
    
    print("SEQUENTIAL EXPRESSION CALCULATOR")
    print("Type '=' to evaluate, 'c' to clear, 'q' to quit")
    print("_" * 50)
    
    expression = ""
    
    while True:
        inp = input(f"\nExpression: {expression if expression else '(empty)'}\n> ").strip()
        
        if inp.lower() == 'q':
            print("Goodbye!")
            break
        
        if inp.lower() == 'c':
            expression = ""
            print("Cleared!")
            continue
        
        if inp == '=':
            if not expression:
                print("Nothing to evaluate!")
                continue
            try:
                result = eval(expression)
                print(f"Result: {result}")
                expression = str(result)
            except ZeroDivisionError:
                print("Error: Division by zero!")
            except Exception as e:
                print(f"Error: {e}")
            continue
        
        expression += inp + " "
        
print(sequential_calculator())