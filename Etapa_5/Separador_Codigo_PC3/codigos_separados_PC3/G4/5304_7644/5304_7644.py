ni = int(input("Numero inicial de bacterias: "))
h = float(input("quantidade de horas total: "))
p =  0.15 
while(h != 0):
	h = h - 1
	ni = int((p * ni)) + ni 
	print(ni)
	