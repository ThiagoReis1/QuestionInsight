#Patrick Chessmam - 21200931

E = float(input("Digite numero de horas extras: "))
F = float(input("Digite numero de horas faltadas: "))
H = E - 2.0/3 * F 

if (E < 0 or F < 0):
	print("Entradas:", E ,"horas extras e", F ,"horas de falta")
	print("Dados invalidos")

elif (H > 2400) :
	G = 500.00
elif (H > 1800) and (H <= 2400) :
	G = 400.00
elif (H > 1200) and (H <= 1800) :
	G = 300.00
elif (H > 600) and (H <= 1200 ) :
	G = 200.00
else :
	(H <= 600) 
	G = 100.00
print("Entradas:", E ,"horas extras e", F ,"horas de falta")
print("Gratificacao: R$", (round(G,2)))	
		
		