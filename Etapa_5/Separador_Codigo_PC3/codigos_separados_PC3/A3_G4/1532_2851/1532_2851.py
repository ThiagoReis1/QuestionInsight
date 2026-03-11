from math import*

x = float(input("Digite um número: "))
k = int(input("Digite um número: "))

i = 1
t = 0
y = 0

while(i < k ):
	x = (x**i)/(factorial(i)) 
	print(x)