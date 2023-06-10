first_num = float(input("insert first value: "))
print(" 1 for addition")
print(" 2 for subtraction")
print(" 3 for multiplication")
print(" 4 for division")
operation = input("select math operation: ")
second_num = float(input("input second value: "))
if operation == "1":
    print ("your answer is: ", (first_num+second_num))
elif operation == "2":
    print ("your answer is: ", (first_num-second_num))
elif operation == "3":
    print ("your answer is: ", (first_num*second_num))
elif operation == "4":
    if second_num == 0.0:
        print ("cannot divide error")
    else:
        print ("your answer is: ", (first_num/second_num))
else:
 print("invalid operation")