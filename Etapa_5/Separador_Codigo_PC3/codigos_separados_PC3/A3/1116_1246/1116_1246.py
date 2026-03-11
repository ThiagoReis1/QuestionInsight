#Karoline Costa
#14 de julho de 2016
#Av. 03 
#Questão 1
x= float(input("Digite a coordenada x: "))
y=float(input("Digite a coordenada y: "))


if(x>0 and y>0):
	mensagem =("estah no quadrante 1")
	if(x<0 and y<0):
		mensagem =("estah no quadrante 3")
		if(x<0 and y>0):
			mensagem =("estah no quadrante 2")
			if(x>0 and y<0):
				mensagem =("estah no quadrante 4")
else:
	mensagem= ("estah situado sobre um dos eixos")
		
			
print("O ponto" ,"(", x ,",", y ,")" , mensagem)


	