from numpy import *
p=(eval(input()))
soma=0
contador=0
for pc in p:
	if pc >180.0:
		soma+=pc
		contador+=1
if contador >0:
	media=round(soma/contador,2)
	print(media)
else:
	print(0.0)
