n= int(input("numero:"))

if (n >= 1):
	if (n % 3 == 0) and (n % 5 != 0):
		m= "Plunct"
	elif (n % 5 == 0) and (n % 3 != 0):
		m= "Plact"
	elif (n % 3 == 0) and (n % 5 == 0):
		m= "Zuuum"
	else:
		m= n
else:
	m= n
print(m)