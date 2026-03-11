#Inserindo o nome da aminoacido desejado
a = input("Calcular qual aminoacido? (Isoleucina/Metionina)").lower()

#Peso moleculares:
#Oxigenio
o = 15.9994
#Carbono
c = 12.011
#Nitrogenio
n = 14.0067
#Enxofre
s = 32.066
#Hidrogenio
h = 1.00794

#Condicional para calcular o peso molecular dos aminoacidos
if (a == "isoleucina"):
	p = (6 * c) + (13 * h) + (1 * n) + (2 * o)
else:
	p = (5 * c) + (11 * h) + (1 * n) + (2 * o) + (1 * s)
	
print(round(p,2))
	
	
	
	
	
	
	
	
	