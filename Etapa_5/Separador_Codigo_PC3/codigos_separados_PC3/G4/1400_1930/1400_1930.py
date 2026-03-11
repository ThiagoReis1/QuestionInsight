tipo= input()
n= int(input())
d1= int(input())
d2= int(input())

if(tipo=="constricao"):
	dano=((d1+d2)+1) * n
	print(dano)
else:
	dano1= d1 * d2
	print(dano1)
