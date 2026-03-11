altura_alice = 1.6
taxa_alice = 0.02


h = float(input("Digite sua altura: "))
taxa = float(input("Digite sua taxa de crescimento: "))
total = h + taxa

t = 0

while(h < altura_alice):
	altura_alice = altura_alice + taxa_alice
	h = h + taxa
	t = t + 1

print(t)