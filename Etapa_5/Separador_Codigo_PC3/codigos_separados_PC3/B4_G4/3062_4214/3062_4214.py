ouro= int(input("Pecas de ouro PO:"))
arma= input("Arma escolhida(ESPADA, MACHADO OU MARRETA):")
dado= int(input("Fator de sucesso(1 a 10):"))

if(arma=="ESPADA" and ouro>=100):
	print(dado*10)
	
elif(arma=="MACHADO" and ouro>=30):
	print(dado+3)
	
elif(arma=="MARRETA" and ouro>=50):
	print(dado+5)
	
elif(dado<1 or dado>10):
	print("Entrada invalida")
	
elif(arma!="MARRETA" and arma!= "ESPADA" and arma!="MACHADO"):
	print("Entrada invalida")

else:
	print("PO insuficiente")
	