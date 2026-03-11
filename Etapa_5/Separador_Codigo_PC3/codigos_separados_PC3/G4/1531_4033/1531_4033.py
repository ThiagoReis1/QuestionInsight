from math import*

x=eval(input("Digite o valor do angulo: "))
k=int(input("Digite a quantidade de termos: "))

i=0
soma=0

while(i<k):
	soma=soma+(((x)**(2*i))/(factorial(2*i)))*(-1)**(i)
	i=i+1
print(round(soma,10))