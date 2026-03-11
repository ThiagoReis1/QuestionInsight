unidade = input("M = m/s e K = km/h: ")
velocidade = float(input("Velocidade: "))

if (unidade == 'M'):
	v = 3.6*velocidade
	
else: 
	v = velocidade/3.6
	
print(round(v,2))
