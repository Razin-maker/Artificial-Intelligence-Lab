num = int (input("Enter a Number to find its Factorial: "))

fact = 1

if num < 0:
    print("Factorial is undefined for negative numbers")
    
elif num == 0 or num == 1:
    print("The factorial of", num, "is 1.")
    
else:
    for r in range(1, num+1):
        fact *= r
    print("The factorial Of", num, "is", fact)