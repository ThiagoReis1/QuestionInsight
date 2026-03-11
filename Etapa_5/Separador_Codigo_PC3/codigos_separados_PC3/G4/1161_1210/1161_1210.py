z=int(input("numero de zumbis z:"))
h=int(input("numero de habitantes h:"))
x=int(input("capacidade de transformar pessoas em zumbis por dia:"))
y=int(input("capacidade de matar zumbis por dia:"))
t=0

while(h > 0):
	z=z-y
	h=h-x*z
	t=t+1
	
print(t)
	
