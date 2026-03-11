x= float(input('numero: '))
if(-100<=x<0):
	v= -1/x
	print(round(v,4))
elif(0<x<=100):
	v= 1/x
	print(round(v,4))
else:
	print('entrada invalida')