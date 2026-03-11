x=float(input("Qual coordenada X?"))
y=float(input("Qual cordenada Y?"))

if (x>0)and(y>0):
	print("O ponto" "(" x","y ")""estah no quandrante 1")
elif(x<0)and(y>0):
	print("O ponto" ""(",x,",",y")estah no quandrante 2")
elif (x<0)and(y<0):
	 print("O ponto (",x,",",y")estah no quandrante 3")
elif(x>0)and(y<0):
	print("O ponto (",x,",",y")estah no quandrante 4")
elif (x==0)and(y==0):
	print("O ponto (",x,",",y")estah situado sobre um dos eixos " )
	
	
