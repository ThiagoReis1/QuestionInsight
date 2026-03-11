s = input("Informe os prodtos comprados, digite H para hortifruti, L para laticinios e E para enlatados: ").upper()

i = 0
acumH = 0
acumL = 0
acumE = 0
total = 0 

while i<len(s):
	if s[i] == "H":
		acumH = acumH + 1
		total = total + 3.85
	elif s[i] == "L":
		acumL = acumL + 1
		total = total + 2.95
	elif s[i] == "E":
		acumE = acumE + 1
		total = total + 7.90
	i = i + 1

print(round(total,2),acumH,acumL,acumE)