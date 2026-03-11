x = float(input())
y = float(input())

if( x == 0 or y == 0):
	print ("o ponto (",x,",",y,") estah num dos eixos")
elif(x>0 and y>0):
	print (" o ponto (",x,",",y,")estah no quadrante 1")
elif(x<0 and y<0):
	print ("o ponto (",x,",",y,") estah no quadrante 3")
elif(x>=0 and y<=0):
	print ("o ponto (",x,",",y,") estah situado sobre um dos eixos")
elif (x<=0 and y>=0):
	print ("o ponto (",x,",",y,") estah situado sobre um dos eixos")