nota1 = float(input("nota 1:"))
nota2 = float(input("nota 2:"))
nota3 = float(input("nota 3:"))
nota4 = float(input("nota 4:"))
nota5 = float(input("nota 5:"))
media = (nota1 + nota2 + nota3 + nota4 + nota5)/5
print (round(media,2))
if (media >= 7.0):
	print ("Aprovacao")
else: 
	print("Reprovacao por nota")