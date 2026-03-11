from numpy import*

candidato = input('informe o candidato: A,B,C ou D: ').upper().split(',')
vet = zeros(4, dtype=int)

for i in range(size(candidato)):
	if candidato[i] == 'A':
		vet[0]= vet[0]+1
	elif candidato[i] == 'B':
		vet[1]= vet[1]+1
	elif candidato[i] == 'C':
		vet[2]=vet[2] +1
	elif candidato[i] == 'D':
		vet[3]=vet[3]+1

print(vet)		
		