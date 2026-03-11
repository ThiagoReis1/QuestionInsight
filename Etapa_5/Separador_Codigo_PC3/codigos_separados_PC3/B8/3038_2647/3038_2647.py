from math import *

entrada = float(input())

if(entrada<= -1.0 or entrada >=1.0):
	resultado = sqrt(abs(entrada))
	print(round(resultado,2))
elif((entrada > -1 and entrada < 0) or(entrada>0.0 and entrada <1)):
	resultado = abs(entrada)
	print(round(resultado,2))
elif(entrada == 0):
	print(0)