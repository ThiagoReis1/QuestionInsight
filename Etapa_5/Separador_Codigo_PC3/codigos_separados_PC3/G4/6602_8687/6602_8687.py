# faça seu código aqui!
n = int(input("Alunos: "))

l = 0
k = 0
p = 0
c = 0

while c < n:
	prato = input("L, C ou P: ").upper()
	if prato == "L":
		l += 1
	elif prato == "C":
		k += 1
	else:
		p += 1
	c += 1
	
print("L=", l)
print("C=", k)
print("P=", p)