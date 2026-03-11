voo = float((input("Tempo de voo: ")))

if(voo > 200):
	resto = voo - 200
	preco = 8000 + (100 * 200) + (90 * resto)
else: 
	preco = 5000 + (100 * voo)
	
print(preco)