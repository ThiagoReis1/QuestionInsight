unidade = input("Unidade: C ou P ?")
unidade = unidade.upper()
medida = float(input("Medida: "))

p = 0.393701*medida
c = medida/0.393701

if(unidade == "P"):
	conversao = medida/0.393701
else:
	conversao = 0.393701*medida
	
print(round(conversao,2))
	