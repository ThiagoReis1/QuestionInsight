from numpy import *
entrada = array(eval(input()))
soma = 0
elementos =0
for i in entrada:
	if(i>180):
		soma +=i
		elementos+=1
if(elementos==0):
	print(0.0)
else:
	media = float(soma/elementos)
	print(round(media,2))