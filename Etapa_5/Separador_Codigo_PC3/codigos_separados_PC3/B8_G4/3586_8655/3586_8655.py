from numpy import *
anel = array(eval(input("Total de aneis acertados")))
i = 0
pont = 0
while i < size(anel):
	if anel[i] == 1:
		pont = pont + 100
	elif anel[i] == 2:
		pont = pont + 60
	elif anel[i] == 3:
		pont = pont + 20
	i += 1
	
print(pont)
	