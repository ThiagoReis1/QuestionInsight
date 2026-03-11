from numpy import *
s = input("Nacionalidade: ").upper()
a = s.split(',')
qtd = zeros(5,dtype=int)

for i in range(size(a)):
	if a[i] == "AR":
		qtd[0] = qtd[0] + 1
	elif a[i] == "BR":
		qtd[1] = qtd[1] + 1
	elif a[i] == "CL":
		qtd[2] = qtd[2] + 1
	elif a[i] == "CO":
		qtd[3] = qtd[3] + 1
	elif a[i] == "UY":
		qtd[4] = qtd[4] + 1
print(max(qtd))
print(qtd)