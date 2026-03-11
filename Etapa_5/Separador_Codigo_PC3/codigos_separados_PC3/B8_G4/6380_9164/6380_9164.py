from numpy import*
p= input("Digite o caractere do produto desejado: ").upper().split(',')
cont = zeros(4, dtype=int)

for i in range(len(p)):
	if p[i] == "E":
		cont[0] += 1
	elif p[i] == "V":
		cont[1]+= 1
	elif p[i] == "A":
		cont[2] += 1
	elif p[i] == "D":
		cont[3]+= 1

print(cont)