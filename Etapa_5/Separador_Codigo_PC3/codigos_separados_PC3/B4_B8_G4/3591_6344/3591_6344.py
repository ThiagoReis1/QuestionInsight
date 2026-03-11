from numpy import*

vet = array(eval(input("digite os dados: ")))

i = 0
acum = 0

while i < size(vet):
	if vet[i] == 1:
		acum = acum + 10
	elif vet[i] == 2:
		acum = acum + 5
	elif vet[i] == 3:
		acum = acum + 10
	elif vet[i] == 4:
		acum = acum + 5
	elif vet[i] == 5:
		acum = acum + 10
	elif vet[i] == 6:
		acum = acum + 5
	i = i + 1
print(acum)