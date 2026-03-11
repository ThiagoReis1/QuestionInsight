from numpy import*

anel = array(eval(input('insira a quantidade de aneis: ')))

i = 0
pont = 0

while i < size(anel):
	if anel[i] == 1:
		pont += 80
	elif anel[i] == 2:
		pont += 40
	elif anel[i] == 3:
		pont += 20
	elif anel[i] == 4:
		 pont += 10
	i += 1
	
	
print(pont)