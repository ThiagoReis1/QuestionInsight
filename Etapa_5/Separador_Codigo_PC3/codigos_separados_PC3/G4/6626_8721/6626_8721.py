# faça seu código aqui!
from numpy import*
c = input("Digite a palavra: ").upper()
i = 0
s = 0

while i < len(c):
	if c[i] == "C" :
		s = s + 1
	i = i + 1
print(s)
