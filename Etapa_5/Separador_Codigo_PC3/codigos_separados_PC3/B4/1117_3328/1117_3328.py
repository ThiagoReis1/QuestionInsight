preco= float(input("valor: "))
dia= int(input("dia da semana: "))
musicaaovivo=input("entre com S ou N: ")
print("Entradas: ",preco,",",dia,",",musicaaovivo)
if((preco<0)and(dia!=1 or dia!=2 or dia!=3 or dia!=4 or dia!=5 or dia!=6 or dia!=7 )and (musicaaovivo!="S" or musicaaovivo!="N")):
	print("Dados invalidos")
else:
	if((preco>=0)and(dia==1)and(musicaaovivo=="S")):
		print("Valor a pagar: R$",preco+20)
	elif((preco>=0)and(dia==2)and(musicaaovivo=="S")):
		print("Valor a pagar: R$",preco+20)
	elif((preco>=0)and(dia==3)and(musicaaovivo=="S")):
		print("Valor a pagar: R$",preco+20)
	elif((preco>=0)and(dia==4)and(musicaaovivo=="S")):
		print("Valor a pagar: R$",preco+20)
	elif((preco>=0)and(dia==5)and(musicaaovivo=="S")):
		print("Valor a pagar: R$",preco+20)
	elif((preco>=0)and(dia==6)and(musicaaovivo=="S")):
		print("Valor a pagar: R$",preco+20)
	elif((preco>=0)and(dia==1)and(musicaaovivo=="N")):
		print("Valor a pagar: R$",preco)
	elif((preco>=0)and(dia==2)and(musicaaovivo=="N")):
		print("Valor a pagar: R$",preco-preco*0.25)
	elif((preco>=0)and(dia==3)and(musicaaovivo=="N")):
		print("Valor a pagar: R$",preco-preco*0.25)
	elif((preco>=0)and(dia==4)and(musicaaovivo=="N")):
		print("Valor a pagar: R$",preco)
	elif((preco>=0)and(dia==5)and(musicaaovivo=="N")):
		print("Valor a pagar: R$",preco-preco*0.25)
	elif((preco>=0)and(dia==6)and(musicaaovivo=="N")):
		print("Valor a pagar: R$",preco)
	elif((preco>=0)and(dia==7)and(musicaaovivo=="N")):
		print("Valor a pagar: R$",preco)
	else:
		print("Dados invalidos")
		
		
