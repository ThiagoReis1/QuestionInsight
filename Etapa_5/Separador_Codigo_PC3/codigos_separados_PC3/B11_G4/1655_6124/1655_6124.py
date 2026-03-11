from numpy import*

cont = zeros(5 ,dtype=int)
vet = input("Estados: ").upper().split(',')

for i in vet[0]:
	if vet == "AC":
		cont = cont + 1
		print(cont)
	if vet == "AM":
		cont = cont + 1
		print(cont)
	if vet == "PA":
		cont = cont + 1
		print(cont)
	if vet == "RO":
		cont = cont + 1
		print(cont)
	if vet == "RR":
		cont = cont + 1
		print(cont)

	