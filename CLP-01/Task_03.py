t_sum = 0

for num in range(50, 101):
    if num % 3 == 0 and num % 5 != 0:
        t_sum += num
        
        
print("The sum of numbers between 50 and 100 divisible by 3 and not divisible by 5 is:", t_sum)
