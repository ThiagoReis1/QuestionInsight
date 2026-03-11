from numpy import*
s = input(" ").upper()
i=0
cont = 0
tam = len(s)
while i < tam:
	if s[i] == "B":
		cont = cont + 1
	i = i +1
print(cont)