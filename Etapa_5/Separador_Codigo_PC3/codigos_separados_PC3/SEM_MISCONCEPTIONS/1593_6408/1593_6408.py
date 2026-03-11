from numpy import *
nota= array(eval(input(':')))

tamanho= len(nota)

soma= 0

i= 0
x= 1
somax= 0
while(i<tamanho):
	soma= soma+ nota[i]*x
	somax= somax+x
	x=x+1
	i= i+1
	
media= soma/somax

print(round(media, 2))