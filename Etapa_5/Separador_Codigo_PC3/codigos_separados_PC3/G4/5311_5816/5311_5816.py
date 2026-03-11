di = float(input(": "))
t = int(input(": "))
fim = t
cont = 0
ac = di
j = 0.012
while(cont != fim):
	ac = ac + ac * j
	cont = cont + 1
	print(round(ac,2))