satisfacao = ''
i = 0
countSim = 0

while(satisfacao != 'S'):
	satisfacao = input().upper()
	
	if(satisfacao == 'SIM'):
		countSim = countSim + 1
	i = i + 1
	
print(i - 1)
print((countSim / (i - 1)) * 100)