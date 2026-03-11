n = input("Responda sim ou nao: ").upper()

ss = 0
nn = 0

while(n != "S"):
	if(n == "SIM"):
		ss = ss + 1
	else:
		nn = nn + 1
	n = input("Responda sim ou nao").upper()
soma = ss + nn
p1 = ss/soma*100
print(round(p1,2))
