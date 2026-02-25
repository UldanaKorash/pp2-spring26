numbers = [10, 5, 23, 7, 15]
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
a = [1, 4, 9]
b = [2, 8, 6]
print("Overall min:", min(min(a), min(b)))
print("Overall max:", max(max(a), max(b)))


nums = [-10, 5, -3, 7]
abs_values = [abs(n) for n in nums]
print("Absolute values:", abs_values)
print("Absolute of -25:", abs(-25))


num1 = 3.14159
num2 = 7.9876
print("Rounded num1:", round(num1))      
print("Rounded num1 to 2 decimals:", round(num1, 2))  
print("Rounded num2 to 1 decimal:", round(num2, 1))   