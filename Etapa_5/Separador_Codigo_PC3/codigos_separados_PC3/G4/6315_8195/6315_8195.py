var1 = input('')
I = 0
M = 0
S = 0
cont = 0
i = 0
while(i<len(var1)):
	if(var1[i] == 'I' ):
		I = I + 1
		cont = cont +  3.75
	if(var1[i] =='M'):
		M = M + 1
		cont = cont + 4.5
	if(var1[i] == 'S'):
		S = S + 1
		cont = cont + 2.90
	i = i + 1
print(round(cont,2),I,M,S)