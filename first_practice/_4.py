result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        num_iter = 0
        while not operand and num_iter <= 3:
            try:
                char = input("1>>> ")
                operand = float(char)
                wait_for_number = False
                
            except ValueError:
                num_iter += 1
                if num_iter > 3:
                    print(f" {char} is not a number. Try again.")
                    
    elif result is None:
        result = operand
        operand = None
        continue
    
    elif not wait_for_number:
        
        num_iter = 0
        while not operator and num_iter <= 3:
            char = input("2>>> ")
            if char in {'+', '-', '/', '*', '='}:
                operator = char
            else:
                num_iter += 1
                if num_iter > 3:
                    print(f"{char} is not '+' or '-' or '/' or '*'. Try again")
                    continue
        
        if operator and not operand:
            wait_for_number = True
                
        if operator and operand:
            if operator == '+':
                result += operand
                operand = None
                operator = None
            elif operator == '-':
                result -= operand
                operand = None
                operator = None
            elif operator == '*':
                result *= operand
                operand = None
                operator = None
            elif operator == '/':
                if operand == 0:
                    print("Division by zero is not allowed.")
                    continue
                else:
                    result /= operand
                    operand = None
                    operator = None
                                
            if not operator and operand:
                wait_for_number = False
            
        if char == "=":
            
            print(f"Result: {result}")
            result = None
            operand = None
            operator = None
            wait_for_number = True
            
            break
            # continue
                    
                