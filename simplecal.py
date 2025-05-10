try:
    a = int(input("Enter first number"))
    b = int(input("Enter Second number"))

    op = input("Enter The Operator \n 1.Addition (+) \n . Subtraction(-) \n 3. Multiply(*)  \n 4.Divide(/)")
    match op:
        case '+':
            print(f"The Sum is {a+b}")
        case '-':
            print(f"The Subtract is {a-b}")
        case '*':
            print(f"The Multiply is {a*b}")
        case '/':
                print(f"The divide is {a/b}")
        case default:
              print(f"There was an Error")

    



except Exception as e:
     print("Enter Valid Input")
