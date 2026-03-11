altura_alice = 1.6
taxa_alice = 0.02

alt = float(input("altura da pessoa: "))
cresc = float(input("taxa de crescimento: "))

anos = 0

while altura_alice > alt:
	altura_alice += taxa_alice
	alt += cresc
	anos += 1
	
print(anos)
