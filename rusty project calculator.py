x = 0


def calculate():
    first_num = float(input("insert first value: "))
    second_num = float(input("input second value: "))
    print(" 1 for addition")
    print(" 2 for subtraction")
    print(" 3 for multiplication")
    print(" 4 for division")
    operation = input("select math operation: ")
    if operation == "1" :
        answer = print("your answer is: ", (first_num+second_num))
    elif operation == "2":
        answer = print("your answer is: ", (first_num-second_num))
    elif operation == "3":
         answer = print("your answer is: ", (first_num*second_num))
    elif operation == "4":
        if second_num == 0.0:
            print("cannot divide error")
        else:
            answer = print("your answer is: ", (first_num/second_num))
    print(answer)
    global x
    x = answer
    another = input("Do you want to run another calculation? (yes/no): ")
    if another == "yes":
        recall()
    elif another == "no":
        print("the end of program")


def calculator():
    next_calculation = input("Let's do a calculation. Shall we? (yes/no): ")
    if next_calculation == "yes":
        calculate()
    elif next_calculation == "no":
        print("the end of program")
    else:
        print("incorrect value")


def recall():
    new_cal = input("do you want to use previous answer? (yes/no): ")
    if new_cal == "yes":
        calculate()
        first_num = x
        second_num = float(input("input second value: "))
        print(" 1 for addition")
        print(" 2 for subtraction")
        print(" 3 for multiplication")
        print(" 4 for division")
        operation = input("select math operation: ")
        if operation == "1":
            print("your answer is: ", float(first_num + second_num))
        elif operation == "2":
            print("your answer is: ", float(first_num - second_num))
        elif operation == "3":
            print("your answer is: ", float(first_num * second_num))
        elif operation == "4":
            if second_num == 0.0:
                print("cannot divide error")
            else:
                print("your answer is: ", float(first_num / second_num))
        print(recall())
    elif new_cal == "no":
        calculator()


cal = calculator()
print(cal)