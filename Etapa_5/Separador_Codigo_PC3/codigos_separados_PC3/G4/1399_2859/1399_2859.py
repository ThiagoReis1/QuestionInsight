ar = float(input("Quant. de Votos para Ambrosio Rutra: " ))
do = float(input("Quant. de Votos para Demelza Olecram: " ))

vt = ar + do

par = (ar/vt)*100
pdo = (do/vt)*100

if(par>pdo):
	print("Ambrosio Rutra")
	print(round(par, 2))
else: 
	print("Demelza Olecram")
	print(round(pdo, 2))