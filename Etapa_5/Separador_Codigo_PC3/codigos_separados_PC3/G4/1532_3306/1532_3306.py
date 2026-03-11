from math import*
x= float(input("digite um numero:"))
k= int(input("digite a quantidade de termos:"))
soma= 0
i= 0
fim= k-1
while(i<=fim):
	soma= soma + (x**((2*i)+1) / (factorial((2*i) +1)))
	i= i+1
print(round(soma, 9))