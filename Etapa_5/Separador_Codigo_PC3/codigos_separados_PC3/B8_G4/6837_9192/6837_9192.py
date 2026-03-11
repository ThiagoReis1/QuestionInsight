from numpy import*

pd = input("Informe o produto: ").upper()
i = 0
pj = 0


I = 3.75
M = 4.50
S = 2.90

while(i < len(pd)):
	if(pd[i] == 'I'):
		pj = pj + I
	elif(pd[i] == 'M'):
		pj = pj + M
	elif(pd[i] == 'S'):
		pj = pj + S
	i = i + 1
	
print(round(pj,2))