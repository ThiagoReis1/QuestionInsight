from numpy import *

s1 = input("Senha:")

i = 0
vogal = 0
consoante = 0 

while (i < len(s1)):
	if (s1[i] == "A") or (s1[i] == "E") or (s1[i] == "I") or (s1[i] == "O") or (s1[i] == "U"):
		vogal = vogal + 1
	else:
		consoante = consoante + 1
	i = i + 1
	
total = (vogal * 3.15) + (consoante * 4.17)

print(round(total,2))