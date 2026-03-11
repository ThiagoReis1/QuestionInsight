l=int(input())
t=int(input())
tl=float(input())
tt=float(input())
cont=1

x=(tl)
y=(tt)
l = l * x + l
t = t * y + t

while (t<l):
	l = l * x + l
	t = t * y + t
	cont=cont+1
	print (cont)