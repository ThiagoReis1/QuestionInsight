n1= float(input("Escrava aqui a nota:"))
n2= float(input("Escrava aqui a nota:"))
n3= float(input("Escrava aqui a nota:"))
n4= float(input("Escrava aqui a nota:"))
n5= float(input("Escrava aqui a nota:"))

media= (n1+n2+n3+n4+n5)/5
print(round(media,1))

if(media>=5):
	print("Aprovado")
	
else :
	print("Reprovado")