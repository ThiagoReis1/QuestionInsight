
hp = float(input())
txcp = float(input())

altura_max = 1.75
taxa_max = 0.01

anos = 0

while hp < altura_max:
	hp += txcp
	altura_max += taxa_max
	
	anos += 1

print(anos)
