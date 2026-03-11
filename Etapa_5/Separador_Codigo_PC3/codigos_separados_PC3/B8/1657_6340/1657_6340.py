from numpy import*
estado = input("Informe o estado: ").upper().split(',')
qtd = zeros(5, dtype = int)
aux = 0

for i in range(len(estado)):
	if(estado[i] == 'AZ'):
		qtd[0] += 1
	elif(estado[i] == 'CA'):
		qtd[1] += 1
	elif(estado[i] == 'FL'):
		qtd[2] += 1
	elif(estado[i] == 'PA'):
		qtd[3] += 1
	elif(estado[i] == 'WI'):
		qtd[4] += 1
		
for i in range(size(qtd)):
	if(qtd[i]>aux):
		aux = qtd[i]
	
print(aux)
print(qtd)