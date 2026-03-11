hc = 1.8
tc = 0.01

cont = 1

hp = float(input())
tp = float(input())

hc = hc + tc
hp = hp + tp

while hp<hc:
	hc = hc + tc
	hp = hp + tp
	cont = cont + 1 
print(cont)