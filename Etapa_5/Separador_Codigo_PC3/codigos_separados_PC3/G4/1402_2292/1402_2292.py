arma = input("machado ou lanca: ")
fts = int(input(" : "))

if (arma == "machado"):
   dano = (30 * (fts/10))
else:
	dano =5 + (20 * (fts/10))
print(int(dano))