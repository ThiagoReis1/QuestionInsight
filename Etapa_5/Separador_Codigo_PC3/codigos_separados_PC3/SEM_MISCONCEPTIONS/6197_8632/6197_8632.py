alt = float(input("a: "))
t = float(input("t: "))
altalice = 1.6
talice = 0.02
cont = 0
while altalice > alt:
	alt = alt + t
	altalice = altalice + talice
	cont = cont + 1
print(cont)

