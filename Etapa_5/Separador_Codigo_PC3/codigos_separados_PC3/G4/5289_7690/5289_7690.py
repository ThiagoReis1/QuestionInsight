d = int(input("face do dado de 1 a 6: "))
cont = 0
lan = 0
while (d != -1):
	d = int(input("face do dado de 1 a 6: "))
	if (d == 6):
		cont = cont + 1
		lan = lan + 1
	 
	else:
		lan = lan + 1 
print(lan)
total = (cont*100)/lan
print(round(total,2))