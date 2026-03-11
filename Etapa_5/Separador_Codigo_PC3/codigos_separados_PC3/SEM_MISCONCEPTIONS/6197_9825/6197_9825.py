altura_alice = 1.6
taxa_alice = 0.02

ac = float(input())
ta = float(input())

anos = 0

while ac < altura_alice:
	altura_alice = altura_alice + taxa_alice
	anos = anos + 1
	ac = ac + ta
print(anos)
	


