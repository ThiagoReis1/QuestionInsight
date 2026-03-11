altura_alice = 1.6
taxa_alice = 0.02

alt = float(input("altura da pessoa: "))
taxa = float(input("taxa de crescimento: "))
anos = 0
altM = alt + taxa 

while altura_alice > alt:
		altura_alice = altura_alice + taxa_alice
		alt = alt + taxa
		anos = anos + 1
	
print(anos)