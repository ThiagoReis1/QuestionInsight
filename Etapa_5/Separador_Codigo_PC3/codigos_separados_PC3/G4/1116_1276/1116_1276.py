x = float(input("diga a coordenada x: "))
y = float(input("diga a coordenada y: "))
if(x == 0 or y == 0):
	print("O ponto (",x,",",y,") estah situado sobre um dos eixos" )
elif(x>0 and y>0):
	print("O ponto (",x,",",y,") estah no quadrante 1" )
elif(x<0 and y>0):
	print("O ponto (",x,",",y,") estah no quadrante 2" )
elif(x<0 and y<0):
	print("O ponto (",x,",",y,") estah no quadrante 3" )
else:
	print("O ponto (",x,",",y,") estah no quadrante 4" )