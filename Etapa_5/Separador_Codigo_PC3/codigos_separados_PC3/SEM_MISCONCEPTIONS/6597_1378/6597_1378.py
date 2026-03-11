# faça seu código aqui!
n = int(input())
cont = 0
contA = 0
contB = 0
contC = 0

while cont < n:
	letra = input()
	if letra.upper() == "A":
		contA += 1
	elif letra.upper() == "B":
		contB += 1
	else:
		contC += 1
	cont += 1

print("A=", contA)
print("B=", contB)
print("C=", contC)