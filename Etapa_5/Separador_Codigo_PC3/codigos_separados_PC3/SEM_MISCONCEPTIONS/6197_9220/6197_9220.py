altura_alice = 1.6
taxa_alice = 0.02

altura_x = float(input())
taxa_x = float(input())

anos = 0


while (altura_x < altura_alice):
	anos += 1
	altura_x = altura_x + taxa_x 
	altura_alice = altura_alice + taxa_alice
	
print(anos)

	