h =  int(input("carga horaria: "))
if( h <= 10):
	v = 50
	b= 500
elif(h>10 and h <=20):
	v=60
	b=600
elif(h>20 and h<=30):
	v = 70
	b = 700
else:
	v = 80
	b = 800
p = h*v+b
print(round(p,2))

	