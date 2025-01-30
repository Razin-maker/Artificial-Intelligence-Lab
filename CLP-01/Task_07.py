def f_largest(a, b):
    return max(a, b)

num1 = float(input("Enter The First Number: "))
num2 = float(input("Enter The Second Number: "))

largest = f_largest(num1, num2)

print("The largest number is: ", largest)
