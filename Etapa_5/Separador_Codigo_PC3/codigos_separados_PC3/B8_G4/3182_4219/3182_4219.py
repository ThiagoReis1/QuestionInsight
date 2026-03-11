from numpy import*
jog = array(eval(input("jogadas: ")))
tam = size(jog)
vet = zeros(10, dtype=int)

for i in range(0,tam,3) :
	if jog[i] == jog[i+1] and jog[i]==jog[i+2] :
			if i == 0 :
				vet[0] = vet[0] + 1
			elif i == 1 :
				vet[1] = vet[1] + 1
			elif i == 2 :
				vet[2] = vet[2] + 1
			elif i == 3 :
				vet[3] = vet[3] + 1
			elif i == 4 :
				vet[4] = vet[4] + 1
print(vet)