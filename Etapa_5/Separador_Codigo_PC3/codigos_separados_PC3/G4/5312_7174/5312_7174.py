x=int(input("quantidades de bacterias  "))
y=int(input("horas  "))
cont=0

while(cont<y):
	x=x+(x*0.02)
	x=int(x)
	cont=cont+1
	
print(x)