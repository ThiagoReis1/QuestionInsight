from numpy import *
var = int(input())

for i in range(var + 1):
	if var < 0:
		break
		
	else:
		print(var)
		var -= 2

		
print("Fim da contagem regressiva!")