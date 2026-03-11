x= int(input("x: "))
k= int(input("k: "))

i=0
s=0
from math import*
while(i<k):

	s= s + (x**(2*i+1))/(factorial(2*i+1))
	i=i+1
	
print(round(s,9))	