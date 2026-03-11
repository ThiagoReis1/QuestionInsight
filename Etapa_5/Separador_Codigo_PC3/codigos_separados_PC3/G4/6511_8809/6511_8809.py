ent=input("letra de A a E: ")
valor=int(input("quantidade de entradas: "))
if ent.upper() == "B":
	P=25.9*valor*0.9
	print(round(P,2))
else:
	P2=25.9*valor
	print(round(P2,2))