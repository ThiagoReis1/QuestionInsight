a=float(input("1 Nota:"))
b=float(input("2 Nota:"))
c=float(input("3 Nota:"))
d=float(input("4 Nota:"))
e=float(input("5 Nota:"))

media=a+b+c+d+e/5
round(media,2)
if	(media>=7):
	m="Aprovacao"
else:
	m="Reprovacao por nota"
print(m)	
