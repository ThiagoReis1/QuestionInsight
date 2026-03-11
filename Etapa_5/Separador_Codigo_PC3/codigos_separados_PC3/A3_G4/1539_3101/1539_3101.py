x= float(input("digite um numero: "))
k= int(input("digite um numero: "))
soma = 0
a= 1+ x
eq= 0
while(eq < x):
	eq=((-1) ** (soma)) * (1/a) + eq
	soma= soma + 1
	a= a +1 
print(round(eq, 7))