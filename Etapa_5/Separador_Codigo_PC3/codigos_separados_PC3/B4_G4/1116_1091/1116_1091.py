X=float(input("Digite o valor do ponto X: "))
Y=float(input("Digite o valor do ponto Y: "))
if (X>0 and Y>0):
	print("O ponto ( ",X," , ",Y," ) estah no quadrante 1")
elif (X<0 and Y<0):
	print("O ponto ( ",X," , ",Y," ) estah no quadrante 2")
elif (X<0 and Y<0):
	print("O ponto ( ",X," , ",Y," ) estah no quadrante 3")
elif (X>0 and Y<0):
	print("O ponto ( ",X," , ",Y," ) estah no quadrante 4")
elif (X==0 and Y<0):
	print("O ponto ( ",X," , ",Y," ) estah situado sobre um dos eixos")
elif (X==0 and Y==0):
	print("O ponto ( ",X," , ",Y," ) estah situado sobre um dos eixos")
else:
	print("Valor invalido")