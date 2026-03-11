#Matheus Rodrigo Cruz Gomes - 21650206
#Engenharia Mecanica
#30/06/2016
p1 = float (input("Digite a nota da primeira prova"))
p2 = float (input("Digite a nota da segunda prova"))
p3 = float (input("Digite a nota da terceira prova"))
a = (p1+p2+p3)/3
if (a>=5) :
	print(round(a,1))
	print("Aprovado")
else :
	print(round(a,1)) 
	print ("Reprovado")		
				