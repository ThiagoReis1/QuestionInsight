#digitar coordenadas
x = float(input("digite uma coordenada: "))
y = float(input("digite uma cordenada: "))
#condição para o primeiro quadrante
if (x > 0) and (y > 0):  
	print("o ponto ("x","y") esta")
	elif (x < 0) and (y < 0):
		print("segundo")
	elif (x > 0) and (y < 0):
		print()