ar = int(input("Ambrosio Rutra: "))
do = int(input("Demelza Olecram: "))

if (ar > do):
	print("Ambrosio Rutra")
	p = (ar / (ar + do)) * 100
	print(round(p, 2))
else:
	print("Demelza Olecram")
	p = (do / (ar + do)) * 100
	print(round(p, 2))
	
	

