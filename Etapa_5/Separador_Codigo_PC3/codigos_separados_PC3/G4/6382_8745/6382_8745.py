from numpy import*
msg = array(eval(input("Digite o numero: ")))
vet = zeros(size(msg),dtype=int)

for i in range(size(msg)):
	if msg[i] == 9:
		vet[i] = (msg[i] - msg[i])**2
	else:
		vet[i] = (msg[i] + 1)**2
print(vet)