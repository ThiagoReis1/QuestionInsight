from numpy import *

salto=array(eval(input("Qual o vetor salto: ")))

recorde=2.5

i=0
achou=0

while i<size(salto):
	if salto[i]>2.5:
		achou+=1
	i+=1
	
print (recorde)
print (achou)