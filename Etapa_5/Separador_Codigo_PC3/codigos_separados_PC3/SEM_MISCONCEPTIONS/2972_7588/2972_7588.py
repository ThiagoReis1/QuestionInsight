pos0 = int(input())
vel0 = int(input())
tempoDesl = int(input())

deslocFinal = pos0 + (vel0 * tempoDesl)

if(deslocFinal >= 1000):
	print(deslocFinal)
	print('Sim')
else:
	print(deslocFinal)
	print('Nao')