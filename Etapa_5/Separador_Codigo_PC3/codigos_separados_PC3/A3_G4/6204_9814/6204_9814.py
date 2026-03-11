am = 1.86
tm = 0.01

ac = float(input('Determine o valor: '))
tc = float(input('Determine o valor: '))

cont = 0
ainc = ac
ainm = am

while ac <= am:
	ac = ac + tc
	am = am + tm
	cont += 1
print(cont)