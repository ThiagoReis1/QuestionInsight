from numpy import*

ent = input("string:").upper().split(",")

aux = zeros(4,dtype=int)

for i in ent:
	if i == 'C':
		aux[0] = aux[0] + 1
	elif i == 'O':
		aux[1] = aux[1] + 1
	elif i == 'P':
		aux[2] = aux[2] + 1
	elif i =='E':
		aux[3] = aux[3] + 1
		
print(aux)