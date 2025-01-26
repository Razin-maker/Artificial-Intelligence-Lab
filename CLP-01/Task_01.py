nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

even_sum = 0
odd_sum = 0

for num in nums:
    if num % 2 == 0:
        even_sum += num
        
    else:
        odd_sum += num


print("Sum Of Even Numbers: ",even_sum)
print ("Sum Of Odd Numbers: ",odd_sum)

