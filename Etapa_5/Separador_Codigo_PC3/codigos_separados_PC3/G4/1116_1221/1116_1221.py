X=float(input("Coordenada:"))
Y=float(input("Coordenada:"))
if((X == 1.0) and (Y == 2.5)):
	print("O ponto", ( X , Y ) ,"estah no quadrante 1")
elif(X == 2.0 and Y == 2.0):
		print("O ponto", ( X , Y ) ,"estah no quadrante 2")
elif(X == -1.0 and Y == -2.5):
		print("O ponto", ( X , Y ) ,"estah no quadrante 3")
elif(X == 1.0 and Y == -2.0):
		print("O ponto", ( X , Y ) ,"estah no quadrante 4")
else:
	print("Invalido")