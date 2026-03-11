alta = 1.8
taxaa = 0.01
cont = 0
alt = float(input("altura: "))
taxa = float(input("taxa: "))
while alta > alt:
	alt = alt + taxa
	cont = cont + 1
	alta = alta + taxaa
print(cont)
