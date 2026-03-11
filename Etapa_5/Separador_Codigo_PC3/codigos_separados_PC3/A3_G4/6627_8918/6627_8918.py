# faça seu código aqui!
from numpy import*
s = input("digite aqui: ").upper()
c = 0
i = 0
t = len(s)

while (i < len(s)):
	if (s[i] == "D"):
		c += 1
	i += 1
print(c)
