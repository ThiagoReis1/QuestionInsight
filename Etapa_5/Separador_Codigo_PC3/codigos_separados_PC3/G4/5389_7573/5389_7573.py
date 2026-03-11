se = input(" ")

i = 0 
ct = 0
while( i < len(se)):
	if(se[i] == "A" or se[i] == "E" or se[i] == "I" or se[i] == "O" or se[i] == "U"):
		ct = ct + 3.15
	else:
		ct = ct + 4.17
	i = i + 1
print(round(ct,2))