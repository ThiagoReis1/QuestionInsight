from numpy import*

v = array(eval(input("notas?")))

i = 0
j=1
numerador=0
denominador=0 

while (i<size(v)):
	numerador= numerador + v[i]*j
	denominador= denominador+ j
	i=i+1
	j=j+1
	
x=numerador/denominador

print(round(x,2))