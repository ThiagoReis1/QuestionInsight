quain = int(input("A quantidade inicial de guerreiros na infantaria: "))
quaca = int(input("A quantidade inicial de guerreiros na cavalaria: "))
perin = float(input("O percentual mensal de crescimento da tropa de infantaria: "))
perca = float(input("O percentual mensal de crescimento da tropa de cavalaria: "))
n = 0
while (quain + quaca < 50000):
	quain = quain + (quain * (perin / 100))
	quaca = quaca + (quaca * (perca / 100))
	n = n + 1
print(n)