prova1= float(input("informe a 1 nota: "))
prova2= float(input("informe a 2 nota: "))
prova3= float(input("informe a 3 nota: "))
prova4= float(input("informe a 4 nota: "))
media= (prova1 + prova2 + prova3 + prova4) / 4
print(round(media, 2))
if(media >= 5.0):
	print("Aprovacao")
	
else:
	print("Reprovacao")
	
		