pa = input().upper()

var = 0

for i in range(len(pa)):
	
	if pa[i] == "A" or pa[i] == "E" or pa[i] == "I" or pa[i] == "O" or pa[i] == "U":
		var += 0.15
		
	else:
		var += 0.17
	
print(round(var, 2))