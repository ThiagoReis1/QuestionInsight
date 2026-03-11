altura = float(input("altura: "))
taxa = float(input("taxa: "))
altura_max= 1.75
taxa_max = 0.01
anos = 0
while(altura<altura_max):
	altura = altura + taxa
	altura_max += taxa_max
	anos += 1
print(anos)