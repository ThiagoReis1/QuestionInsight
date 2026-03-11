nummi = int(input("Qual o numero de espigas de milho compradas?"))

if nummi < 6:
	tot=nummi*1.85
else:
	tot=nummi*1.50
	
print(round(tot,2))