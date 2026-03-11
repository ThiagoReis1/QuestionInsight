linguagem = input("(P) phyton, (C), (A) ambas linguagens: ").upper()

contagem = 0 
ambas = 0

while linguagem != "X":
	if linguagem == "A":
		ambas +=1
	linguagem = input("(P) phyton, (C), (A) ambas linguagens: ").upper()

print(ambas)
