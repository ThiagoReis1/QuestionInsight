P = float(input("Digite o peso: "))
if(P >= 5000):
   custo = 0.04 * P + 60
else: 
	custo = (0.05 * P) 
print(round(custo, 2))

