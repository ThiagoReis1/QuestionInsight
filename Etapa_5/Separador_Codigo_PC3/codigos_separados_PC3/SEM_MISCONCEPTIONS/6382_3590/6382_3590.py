entrada = eval(input())
print("[",end='')

for i in range(len(entrada)):
	if(entrada[i] == 9):
		entrada[i] = -1
	if(i == len(entrada) -1):
		print((entrada[i] + 1) * (entrada[i] + 1),end="]")
	else:
		print((entrada[i] + 1) * (entrada[i] + 1),end=' ')