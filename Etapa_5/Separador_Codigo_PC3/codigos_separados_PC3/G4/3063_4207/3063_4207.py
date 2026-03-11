po=int(input("Insira a quantidade de pedras de ouro: "))
arma=input("Escolha: (MALHA); (PLACA; (INTEIRA) => ")
d=int(input("Fator de destreza(1-8): "))

if((d>=1 or d<=8) and (arma=="INTEIRA" or arma=="MALHA" or arma=="PLACA")):
	
		if(arma=="INTEIRA" and po>=50):
			resis=int((30*d)-20)
			print(resis)
		elif(arma=="MALHA" and po>=50):
			resis= int((15*d)-1)
			print(resis)
		elif(arma=="PLACA" and po>=50):
			resis= int((20*d)-18)
			print(resis)
		else: 
			print("PO insuficiente")
else:
	print("Entrada invalida")
			
		
		