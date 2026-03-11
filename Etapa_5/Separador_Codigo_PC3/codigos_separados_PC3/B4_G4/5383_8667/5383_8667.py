from numpy import*

s = input("Digite a string: ").upper()

cust = 0

for i in range(len(s)):
	if (s[i] == "A"):
		cust = cust + 0.12
	elif (s[i] == "E"):
		cust = cust + 0.12 
	elif (s[i] == "I"):
		cust = cust + 0.12
	elif (s[i] == "O"):
		cust = cust + 0.12
	elif (s[i] == "U"):
		cust = cust + 0.12
	else:
		cust = cust + 0.18
		
print(round(cust,2))
	
		
		