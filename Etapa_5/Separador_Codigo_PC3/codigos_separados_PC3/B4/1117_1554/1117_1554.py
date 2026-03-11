preco=float(input("Preco da entrada: "))
dia=int(input("Dia da semana: "))
musica=input("Musica ao vivo (S/N): ")
print("Entradas:", preco, ",", dia, ",", musica)

if(preco<=0 and ((dia<1)or(dia>7))):
	print("Dados invalidos")
elif((dia==2) or (dia==3) or (dia==5)):
	total= preco - (preco*0.25)
	print("Valor a pagar: R$", round(total,2))
elif((dia==2) and (musica=="S")):
	total= (preco - (preco*0.25)) + 20
elif((dia==3) and (musica=="S")):
	total= (preco - (preco*0.25)) + 20
	print("Valor a pagar: R$", round(total,2))
elif((dia==5) and (musica=="S")):
	total= (preco - (preco*0.25)) + 20
	print("Valor a pagar: R$", round(total,2))
else:
	print("Dados invalidos")