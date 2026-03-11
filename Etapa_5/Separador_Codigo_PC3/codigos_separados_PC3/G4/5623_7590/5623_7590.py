x = input("bolo ou salgado: ")
qbs = int(input("quantidade b ou s: "))
qc = int(input("quantidade cappuccinos: "))

if(x=="B"):
	ms= (5 * qbs) + (qc * 7.5)
	
else:
	ms= (4 * qbs) + ( qc * 7.5)
	
print(round(ms,2))
	