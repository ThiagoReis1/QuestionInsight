valor = float(input("digite o valor do ingresso:"))
dia = int(input("digite o dia da semana:"))
mus = input("E dia de musica ao vivo: (S/N):")

print("Entradas:", valor,"," ,dia, ",", mus,)

if (valor >= 0):
	if(dia == "2" or dia == "3" or dia =="5") and ( mus == "N" or mus == "n"):
			preco = valor * 1.25
			preco1 = round(preco, 2) 
		print("Valor a pagar: R$",preco1)
	elif ( dia == "4" or dia == "6" or dia == "1" or dia == "7") and (mus == "N" or mus =="n"):
			preco = valor 
			preco1 = round(preco, 2) 
		print("Valor a pagar: R$",preco1)
	elif (dia == "2" or dia == "3" or dia =="5") and (mus == "s" or mus == "S"):
			preco = valor * 1.25 + 20.00
			preco1 = round(preco1, 2) 
		print("Valor a pagar: R$", preco1)
	elif ( dia == "4" or dia == "6" or dia == "1" or dia == "7") and (mus == "S" or mus =="s"):   
			preco = valor + 20.00
			preco1 = round(preco, 2) 
		print("Valor a pagar: R$", preco1)
else:
	print("Dados invalidos")
		
		
		