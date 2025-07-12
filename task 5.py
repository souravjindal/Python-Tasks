#Task 1: Calculate Factorial Using a Function 


num=int(input("Enter the number:"))
def factorial(num):
    if num<2:
        return 1
    else:
        return num * (factorial(num-1))
output=factorial(num)
print(output)
