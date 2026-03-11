x=float(input("valora:"))
k=int(input("valorb:"))
cont=0
expoente=1
resposta=0
denominador=1
while (cont<k):
	resposta= resposta +(x**expoente)/denominador
	cont=cont+1
	expoente=expoente+1
	denominador=denominador+1
print(round(resposta-x, 10))