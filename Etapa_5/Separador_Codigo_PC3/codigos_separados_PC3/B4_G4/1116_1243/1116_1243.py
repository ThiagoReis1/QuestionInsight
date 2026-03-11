
X = float(input("digite a coordenada X:"))
Y = float(input("digite a coordenada Y:"))

if(((X == 1.0) and (Y == 2.5)) or ((X>0) and (Y>0))):
	print("O ponto", "(", X, ",", Y, ")", "estah no quadrante 1")

elif (((X == -1.0) and (Y == - 2.5)) or ((X<0) and (Y<0))):
	print("O ponto", "(", X, ",", Y, ")", "estah no quadrante 3")
elif ((X == 1.0) and (Y == - 2.0)) or ((X>0) and (Y<0)):
	print("O ponto", "(", X, ",", Y, ")", "estah no quadrante 4")
elif (((X == 0.0) and (Y < 0)) or((X == 0.0) and (Y > 0)) or ((X>0) and (Y == 0)) or ((X<0) and (Y == 0))):
	print("O ponto", "(", X,",", Y, ")", "estah situado sobre um dos eixos")
elif ((X == 0.0) and (Y == 0.0)):
	print("O ponto", "(", X, ",", Y, ")", "estah situado sobre um dos eixos")
else:
	print("O ponto", "(", X, ",", Y, ")", "estah no quadrante 2")