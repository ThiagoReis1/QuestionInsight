from numpy import*

x = input("Digite a sigla do estado: ").split(',')
y = zeros(5 , dtype=int)

AC = 0
AM = 0
PA = 0
RO = 0
RR = 0

for i in x:
	if (i.upper() == "AC"):
		AC = AC + 1
	elif (i.upper() == "AM"):
		AM = AM + 1
	elif (i.upper() == "PA"):
		PA = PA + 1
	elif (i.upper() == "RO"):
		RO = RO + 1
	elif (i.upper() == "RR"):
		RR = RR + 1
		
y[0] = AC
y[1] = AM
y[2] = PA
y[3] = RO
y[4] = RR

print(max(y))
print(y)