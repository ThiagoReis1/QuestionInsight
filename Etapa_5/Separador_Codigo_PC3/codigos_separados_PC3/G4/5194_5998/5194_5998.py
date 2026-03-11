c = input("classification: ").upper()
v = float(input("valor: "))

if c == "A":
	print("Classe: Jounin")
	i = v-(0.22*v)
	
else:
	print("Classe: Chunin")
	i = v-(0.15*v)
	
print(round(i,2))