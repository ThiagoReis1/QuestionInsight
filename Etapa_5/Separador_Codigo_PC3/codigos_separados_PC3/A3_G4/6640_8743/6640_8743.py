# faça seu código aqui!
from numpy import*
v = input("Digite uma letra: ").upper()
c = 0
i = 0
t= len(v)
while (i < len(v)):
	if(v[i] == "N"):
		c += 1
		print(i)
	i += 1
if (c == 0):
	print("nao achei")

	