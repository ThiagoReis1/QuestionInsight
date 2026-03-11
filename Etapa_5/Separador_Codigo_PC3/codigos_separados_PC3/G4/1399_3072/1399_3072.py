A = int(input("quantidade de votos: "))
D = int(input("quantidade de votos: "))

if (A > D):
	print("Ambrosio Rutra")
	p = (A / (A + D)) * 100
	print(round(p, 2))
	
else:
	print("Demelza Olecram")
	p = (D / (A + D)) * 100
	print(round(p,2))
	
	
	


	
	
	
