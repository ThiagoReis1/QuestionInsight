# faça seu código aqui!
from numpy import*
n= input("").upper()
i=0
c=0
while i < len(n):
	if n[i] == "D":
		c+=1
	i+=1
print(c)
	