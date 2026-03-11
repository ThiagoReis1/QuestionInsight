from numpy import*

v1= input("nome do produto: ")
v2=array(eval(input("quantidade: ")))


arroz= 1.25
feijao= 2.60
bis= 1.80
miojo= 0.85
fanta= 3.20

i = 0
soma= 0

while i < size(v1):
	if (v1[i] == "ARROZ"):
		soma= soma + arroz * v2[i]
	elif (v1[i] == "FEIJAO"):
		soma = soma + feijao * v2[i]
	elif (v1[i] == "BIS"):
		soma = soma + bis * v2[i]
	elif (v1[i] == "MIOJO"):
	   soma = soma + miojo * v2[i]
	elif (v1[i] == "FANTA"):
		soma = soma + fanta * v2[i]
		
	i= i + 1
print(round(soma, 2))