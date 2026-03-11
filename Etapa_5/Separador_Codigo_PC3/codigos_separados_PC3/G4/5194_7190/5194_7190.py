m = input("classe (A/B): ").upper()
v = float(input("valor:"))

a = "Jounin"
b = "Chunin"

if(m == "A"):
	i = v*0.22
	print("Classe: ",a)
	print(round(v - i,2))
if(m == "B"):
	i = v*0.15
	print("Classe: ",b)
	print(round(v - i,2))
