altura_chico = 1.5
taxa_chico = 0.02

alturaP = float(input("Altura da outra pessoa: "))
taxaP = float(input("Taxa de crescimento da outra pessoa: "))

anos = 0 

while alturaP < altura_chico:
	alturaP += taxaP
	altura_chico += taxa_chico
	anos += 1
print(anos)