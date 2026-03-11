from numpy import *

vetn = array(eval(input("Vetor de numeros: ")))

i = 0
pont = 0
while size(vetn) > i:
	if vetn[i] == 1:
		
		pont = pont + 100
	elif vetn[i] == 2:
		
		pont = pont + 60
	elif vetn[i] == 3:
		
		pont = pont + 20
	else:
		pont = pont + 0
	i = i + 1
print(pont)	