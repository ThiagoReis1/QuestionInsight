from numpy import*

saques = array(eval(input("Saques: ")))

#Quantos saques foram efetuados em um valor <= 50?
#Indices desses saques

quanti = 0
j = 0

for i in range(size(saques)):
	if saques[i] <= 50:
		quanti += 1

base0 = zeros(quanti, dtype = int)

for i in range(size(saques)):
	if saques[i] <= 50:
		base0[j] = i
		j += 1

print(quanti)
print(base0)
