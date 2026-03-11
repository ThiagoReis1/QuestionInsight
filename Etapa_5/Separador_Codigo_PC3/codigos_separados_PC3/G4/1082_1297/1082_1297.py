# Bianca de Oliveira Cavalcante
#30/06/2016

p1=float(input("nota da prova 1"))
p2=float(input("nota da prova 2"))
p3=float(input("nota da prova 3"))
p4=float(input("nota da prova 4"))
p5=float(input("nota da prova 5"))

media=((p1+p2+p3+p4+p5)/5)
print(round(media,1))

if(media >= 5):
	print("Aprovado")
else:
	print ("Reprovado")

