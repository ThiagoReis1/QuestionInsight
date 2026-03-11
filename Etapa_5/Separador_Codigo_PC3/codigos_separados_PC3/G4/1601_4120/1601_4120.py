from numpy import *

vc = array(eval(input("Digite o tempo de chegada: ")))

i = 0
a = min(vc)
if(vc[i] == a):
	print(i)
while(vc[i] != a):
	i = i + 1
	if(vc[i] == a):
		print(i)
	
		
		


	
	
	