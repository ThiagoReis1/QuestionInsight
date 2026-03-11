 
p1 = float(input("notas: "))
p2 = float(input("notas: "))
p3 = float(input("notas: "))

media = (p1 + p2 + p3) / 3

if (media >= 6):
   
	mensagem = ("Aprovacao")
else:

	mensagem = ("Reprovacao")
	
print(round(media  ,  2))
print(mensagem)



