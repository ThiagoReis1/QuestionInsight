altura_alice = 1.6
taxa_alice = 0.02

altura = float(input())
taxa = float(input())

count = 0

while (altura < altura_alice):
	altura_alice = altura_alice + taxa_alice
	altura = altura + taxa
	
	count += 1
print(count)