ac = 1.5
tc = 0.02
cont = 0

al = float(input())
ala = float(input())

while al < ac:
	al = al + ala
	ac = ac + tc
	cont  = cont + 1
	
print(cont)