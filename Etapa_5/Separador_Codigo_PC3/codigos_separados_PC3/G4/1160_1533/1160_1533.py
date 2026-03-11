h = int(input("numero de habitantes: "))
v = int(input("vampiros: "))
x = int(input("pessoas transformadas em vamp: "))
y = int(input("pessoas q matam vamp: "))
dia = 0
while(h >0 ):
	v = v * x
	v = v - y
	h = h - v
	dia = dia +1
print(dia)