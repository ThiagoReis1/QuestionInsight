preco= float(input())
semana= int(input())
musica= input()
print("Entradas:" "precofinal", 3, "S")

if(preco>=0) and (semana>=1) and (semana<=7) and (musica.upper()=="S" or musica.upper()=="N"):
	if(musica.upper()=="S"):
		precofinal=preco+20-(preco*0.25)
		print("Valor a pagar: R$",round(precofinal,2))
	else:
		if(semana==2 or semana==3 or semana==5):
			precofinal=preco-(preco*0.25)
			print("Valor a pagar: R$",round(precofinal,2))
		else:
			print("Valor a pagar: R$",round(preco,2))
else:
	print("Dados invalidos")
		
	
		
	