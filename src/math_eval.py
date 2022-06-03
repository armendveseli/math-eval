def eval_math(expression: str):
    #Check for no numbers.
    if not any(char.isdigit() for char in expression):
        return 0
    
    #Check for letters (upper and lower case)
    elif any(char.isalpha() for char in expression.lower()):
        return 0
		
    #Check for operators.
    elif not any(sub_str in ["+", "-", "*", "/", "%", "//", "**"] for sub_str in expression):
        return 0

    #Everything seems secure.
    try:
        return eval(expression)
    except:
        raise ArithmeticError("Invalid expression.")
