import math
numbers = [4, 9, 16, 25]
roots = [math.sqrt(n) for n in numbers]
print("Square roots:", roots)


import math
angle_deg = 30
angle_rad = math.radians(angle_deg)  
print(f"sin({angle_deg}) =", math.sin(angle_rad))
print(f"cos({angle_deg}) =", math.cos(angle_rad))
half_circle = math.pi
print("Half circle in radians:", half_circle)


import math
print("Euler's number e:", math.e)
x = 2
print(f"e^{x} =", math.exp(x))