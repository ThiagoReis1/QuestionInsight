valor = float(input("Qual o valor da mensalidade?"))
criancas = int(input("Qual o numero de criancas?"))

d1 = (valor*10)/100
d2 = (valor*30)/100
d3 = (valor*40)/100

if(criancas == 1):
	print(round((valor-d1)*criancas, 2))
elif(criancas == 2):
	print(round((valor-d2)*criancas, 2))
elif(criancas >= 3):
	print(round((valor-d3)*criancas, 2))
else:
	print("Invalido")