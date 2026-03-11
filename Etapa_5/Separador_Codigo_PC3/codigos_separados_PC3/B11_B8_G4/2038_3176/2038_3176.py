n = input('digite s ou n:')

SIM = 0
NAO = 0

while (n != 'S'):
	if (n == 'SIM' and SIM == 0):
		SIM = SIM + 1
	n = input('digite s ou n:')
	if (n == 'SIM'):
		SIM = SIM + 1
	elif (n == 'NAO'):
		NAO = NAO + 1 

print (SIM)		

