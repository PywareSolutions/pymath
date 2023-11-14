def add(*args):
        res = sum(args)
        return res

def subtract(num1, num2):
        res = num1 - num2
        return res

def multiply(num1, num2):
        res = num1 * num2
        return res

def divide(num1, num2):
        res = num1 / num2
        return res

def floor_divide(num1, num2):
        res = num1 // num2
        return res

def math(num1, op, num2):
        if op == "+":
                res = sum(num1, num2)
                return res
        elif op == "-":
                res = num1 - num2
                return res
        elif op == "*" or op.lower == "x":
                res = num1 * num2
                return res
        elif op == "/":
                res = num1 / num2
                return res
        elif op == "//":
                res = num1 // num2
                return res
        else:
                print("Error. Operator unknown. Try again.")
