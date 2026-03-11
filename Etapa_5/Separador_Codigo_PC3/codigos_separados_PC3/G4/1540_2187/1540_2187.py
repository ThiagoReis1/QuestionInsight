from math import *

x = eval(input("x: "))
k = int(input("k: "))

i = 1

cosSqrtX = 1

while(i < k):
	cosSqrtX = cosSqrtX + (x**i)/(factorial(2*i)) * (-1)**(i)
	i = i + 1
print(round(cosSqrtX, 6))