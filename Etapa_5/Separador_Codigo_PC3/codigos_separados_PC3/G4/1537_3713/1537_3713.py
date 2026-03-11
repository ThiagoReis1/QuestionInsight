from math import* 
x = eval(input())
k = int(input())
soma=0
i=0

while i<k:
	soma=soma+(x**(1*i))/(factorial(1*i))
	i+=1
	
	
print(round(soma, 9))
	