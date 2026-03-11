from math import *
x= float(input("entrada numero real: "))
l= int(input("entrada de k:"))
contador = 0
sinal = 1
ser = 0
while(contador<l):
	ser = ser + (1*sinal) * x ** contador
	sinal= -sinal
	contador=contador+1
print(round(ser, 7))
