altura_alice = 1.6
taxa_alice = 0.02
altura = float(input("a.i:"))
taxa = float(input("t.c"))
ano = 0 
while altura < altura_alice:
	altura_alice+=taxa_alice
	altura+=taxa
	ano += 1 
print(ano)