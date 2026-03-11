from math import*
x=float(input("Digite: "))
k=int(input("Digite: "))

var=2
i=1
soma=2


while(soma <= k):
	var= var + 2
	i= i - ((1-(x**var)/(factorial(var))))
	soma= soma +1
	
print(round(soma,8))
	
	
	
	
