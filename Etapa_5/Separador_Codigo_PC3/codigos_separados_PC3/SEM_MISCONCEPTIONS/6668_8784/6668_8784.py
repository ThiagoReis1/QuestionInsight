from numpy import *

mm = eval(input(":"))
soma = 0
contador = 0

for p in mm:
	if p >170:
		soma+= p
		contador+=1
if contador >0:
	mm=round(soma/contador,2)
	print(mm)
else:
	print(0.0)
	
		

		