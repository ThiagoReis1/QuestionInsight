import math 
x=int(input("numero: "))
k=int(input("quantidade da serie: "))

i=0
soma=0

while (i<k):
	soma=soma+( ((x)**(2*i+1))/math.factorial(2*i+1) )
	i=i+1
print(round(soma,9))
	