alt = float(input("altura: "))
tc = float(input("taxa crescimento: "))
aj = 1.77
tj = 0.02
conta = 0
while (alt < aj):
	alt += tc
	aj += tj
	conta += 1
print(conta)