from numpy import*

name = input(" ")
cus = 0
i = 0

while (i<len(name)):
	if ((name[i] == "A") or (name[i] == "E") or (name[i] == "I") or (name[i] =="O") or (name[i] == "U")):
		cus = cus + 3.15
		i +=1
	else:
		cus = cus + 4.17
		i +=1
	
print(round(cus,2))