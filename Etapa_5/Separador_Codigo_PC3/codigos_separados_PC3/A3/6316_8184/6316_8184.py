from numpy import*
string = input("D S I")
cont1 = 0
cont2 = 0
cont3 = 0
D = 2.25
S = 4.00
I = 6.90
i = 0 
valort = 0
tam = len(string)
while (i < tam):
	if (string[i] == "D"):
		cont1 = cont1 + 1
		valort = valort + 2.25
	if (string[i] == "S"):
		cont2 = cont2 + 1
		valort = valort + 4.00
	if (string[i] == "I"):
		cont3 = cont3 + 1
		valort = valort + 6.90
	i = i + 1
print(round(valort,2),cont1,cont2,cont3)


