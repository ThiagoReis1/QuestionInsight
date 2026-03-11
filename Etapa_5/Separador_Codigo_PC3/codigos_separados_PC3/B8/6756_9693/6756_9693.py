# faça seu código aqui!
dias=int(input())
if dias<15:
	taxa= 20.00
elif dias==15:
	taxa=16.00
elif dias>15:
	taxa=10.00
total=(175.00*dias)+taxa
print(round(total,2))