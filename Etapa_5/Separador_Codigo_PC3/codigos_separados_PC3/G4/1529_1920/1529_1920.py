inf = int(input("Infantaria: "))
cav = int(input("Cavalaria: "))
pinf = float(input("% infantaria: "))
pcav = float(input("% cavalaria: "))
i = 0
#-----------------------------------------
while (not(inf + cav >= 50000)):
	inf += inf*pinf/100
	cav += cav*pcav/100
	i +=1
print(i)