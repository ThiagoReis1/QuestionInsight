# faça seu código aqui!

entrada = input("(A/B/C/D/E) : ")
qntde = float(input("Quantidade de entradas : "))

v1 = qntde * (25.9)
v2 = qntde * (90/100 * 25.9) 

if (entrada.upper() == "B") :
	print(round(v2,2))
	
else :
	print(round(v1,2))