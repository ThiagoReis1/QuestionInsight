from numpy import*

ent = array(eval(input("faces:")))

i = 0
soma = 0

while i < size(ent):
	if ent[i] == 1:
		soma = soma + 10
	elif ent[i] == 2:
		soma = soma + 5
	elif ent[i] == 3:
		soma = soma + 0
	elif ent[i]	== 4:
		soma = soma + 5
	elif ent[i] == 5:
		soma = soma + 20
	elif ent[i] == 6:
		soma = soma + 10
		
	i = i + 1
	
print(soma)