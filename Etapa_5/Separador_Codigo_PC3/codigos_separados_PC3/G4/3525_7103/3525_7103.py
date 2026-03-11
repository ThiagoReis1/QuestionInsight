x = float(input())
k = int(input())
sen= 0
i = 0
from math import*
while i<k:
	sen = sen + x**(2*i+1)/factorial(2*i+1)
	i = i+1
	
print(round(sen,9))