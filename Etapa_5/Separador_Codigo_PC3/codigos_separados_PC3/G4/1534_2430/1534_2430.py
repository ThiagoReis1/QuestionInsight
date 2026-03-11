from math import*
x = float(input(""))
k = int(input(""))
arctgh = 0
n=1


while (n<k and -1<x<1):
	arctgh += ((x**n)/n)
	n = n + 2
	
print(round(arctgh,7))