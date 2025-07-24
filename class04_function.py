# def sum(a, b) :
#     result = a + b
#     return result

# a = int(input("Number 1: "))
# b = int(input("Number 2: "))

# result = sum(a, b)
# print("Result: ", result)

def cal(num1, num2, oper) :
    if oper == 1 :
        result = num1 + num2
    elif oper == 2 :
        result = num1 - num2
    elif oper == 3 :
        result = num1 * num2
    elif oper == 2 :
        result = num1 / num2
    else :
        result = "Please try again"
    
    return result

def add(num1, num2) :
    result = num1 + num2
    return result

def minus(num1, num2) :
    result = num1 - num2
    return result

def mutiple(num1, num2) :
    result = num1 * num2
    return result

def divide(num1, num2) :
    result = num1 // num2
    return result

def isEven(result) :
    if (result % 2) > 0 :
        isEven = "even"
    else :
        isEven = "odd"
    
    return isEven

def main() :
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print("Choose your operation: ")
    print("[1]: +")
    print("[2]: -")
    print("[3]: x")
    print("[4]: /")
    oper = int(input("Enter choice: "))
    # result = cal(num1, num2, oper)
    if oper == 1 :
        result = add(num1, num2)
    elif oper == 2 :
        result = minus(num1, num2)
    elif oper == 3 :
        result = mutiple(num1, num2)
    elif oper == 4 :
        result = divide(num1, num2)
    else :
        print("Please try again")
    
    print("Result: ", result)
    print("The result number is", isEven(result), "number")

main()
