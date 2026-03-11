x=float(input())
y=float(input())
z=float(input())
a=float(input())

media=(x+y+z+a)/4
p=round(media,1)
if	(media>=6):
	print(p,"Aprovado")
else:
	print(p,"Reprovado")