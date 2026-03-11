from numpy import*
vd = eval(input())
danos = 0
cont = 0
for i in vd:
	cont = cont + 1
	danos = danos + i*cont
		
print(danos)