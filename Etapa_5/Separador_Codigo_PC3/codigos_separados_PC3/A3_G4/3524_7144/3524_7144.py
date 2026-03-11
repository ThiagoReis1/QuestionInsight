from math import*

x = float(input(""))
k = int(input(""))

soma = 0
i = 0
while(i != 0):
	if(k > 0):
		i = i + 2
		soma = (x/factorial(i))
		print(round(soma,8))	
else:
	soma = (x/1)
	print(round(soma,8))