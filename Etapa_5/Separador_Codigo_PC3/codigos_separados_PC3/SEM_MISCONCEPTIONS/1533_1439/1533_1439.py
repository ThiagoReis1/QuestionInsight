from math import*
x= float(input("digite o valor real de x :"))
k= int(input("digite a quantidade de termos: "))
soma=0
nsoma=0
t=0
while(t<k):
	soma= soma + ((x**(2*t))/(factorial(2*t))
	t=t+1
	nsoma=soma+1
print(round(nsoma,8))