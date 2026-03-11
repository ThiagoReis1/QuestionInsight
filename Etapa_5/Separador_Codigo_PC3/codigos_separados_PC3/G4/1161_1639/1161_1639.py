z=int(input("digite aqui o numero de zumbis que invadiu a vila:"))
h=int(input("digite aqui o numero de habitantes da vila:"))
x=int(input("digite aqui a capacidade de transformaçao:"))
y=int(input("digite aqui a capacidade de exterminio:"))

nz=z
d=1
while(nz<h):
	nz=nz*x-y
	d=d+1
print(d)