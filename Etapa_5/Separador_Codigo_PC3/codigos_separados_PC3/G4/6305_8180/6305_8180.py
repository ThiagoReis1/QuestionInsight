from numpy import*
s = input("H,L,E: ").upper()
H = 3.85
L = 2.95
E = 7.90
cont = 0
cont1 = 0
cont2 = 0
i = 0 
vt = 0
while(i < len(s)):
	if (s[i] == "H"):
		cont = cont + 1
		vt = vt + H
	if (s[i] == "L"):
		cont1 = cont1 + 1
		vt = vt + L
	if (s[i] == "E"):
		cont2 = cont2 + 1
		vt = vt + E
	i = i + 1
print(round((vt),2), cont,cont1,cont2)