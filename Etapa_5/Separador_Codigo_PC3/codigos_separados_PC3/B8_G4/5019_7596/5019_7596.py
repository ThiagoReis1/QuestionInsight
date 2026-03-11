s = float(input("salario atual: "))

if (0<s):
	if (s<1212):
		sf = s * 112 / 100
		print(round(sf,2))
	elif (1212<=s<=5000):
		sf = s * 108 / 100
		print(round(sf,2))
	elif (5000<s):
		sf = s * 103 / 100
		print(round(sf,2))
		
else:
	print("salario nao existe")