l = int(input("Número de Lambaris: "))
t = int(input("Número de tambaquis: "))

taxa_l = float(input("Taxa de crescimento de lambari: "))
taxa_t = float(input("Taxa de crescimento de tambaqui: "))

lambari = l
tambaqui = t

tempo = 1

while(l == t):
	lambari = l * taxa_l - 2 * t + lambari * tempo
	tambaqui = t * taxa_t + tambaqui * tempo
	tempo = tempo + 1
	
print(tempo)