# faça seu código aqui! 
p = 28.5
h = float(input("Em que hora os pratos foram pedidos?: "))
q = float(input("Qual e a quantidade de pratos?: "))
if (h>=18):
	v = (p*q)-p*q*20/100
	print(round(v,2))
else:
	v = q*p
	print(round(v,2))
