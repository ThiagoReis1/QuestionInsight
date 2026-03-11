x= float(input("Numero inicial de copias HIV no sangue:"))
y =float(input("Taxa de reducao:"))
z =float(input("Numero de copias por semana:"))


c=0


while (1000000>x):
	x = (x-(x*y)) + z
	c+=1
	
	
print((c+1))
	