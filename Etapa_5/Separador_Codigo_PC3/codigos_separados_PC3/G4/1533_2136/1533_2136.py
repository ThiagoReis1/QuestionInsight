from math import*
x = float(input("x = "))
k = int(input("k = "))

n = 0
while(k > 0):
   c = ((x**2*n)/factorial(2*n))
   n = n + k
print(round(c , 8))