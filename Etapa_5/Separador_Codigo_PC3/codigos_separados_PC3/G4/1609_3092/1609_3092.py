from numpy import *

dc = array(eval(input("palavras no ceboles?")))

pn= input("palavra correta?")
pn=pn.upper()
pn=pn.replace('R','L')

i=0

while (i< size(dc)) :
	if (dc[i] == pn):
		print(i)
		i= size(dc)+1
	else:
		i=i+1
		if( i >= size(dc)):
			print("NAO ENCONTRADA")

	
