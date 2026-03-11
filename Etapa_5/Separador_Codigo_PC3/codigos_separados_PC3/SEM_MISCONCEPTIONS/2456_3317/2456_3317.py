mensalidade = float(input("valor da mensalidade: "))
numero = int(input("numero de criancas: "))

if(numero == 1):
	valortotal = mensalidade*numero - (mensalidade*10/100)*numero
	print(round(valortotal, 2))
elif(numero == 2):
	valortotal = mensalidade*numero - (mensalidade*30/100)*numero
	print(round(valortotal, 2))
else:
	valortotal = mensalidade*numero - (mensalidade*40/100)*numero
	print(round(valortotal, 2))
				 