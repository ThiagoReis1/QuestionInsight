h=float(input())
t=float(input())
hm = 1.75
tm = 0.01

h=(h+t)
hm=(hm+tm)
cont=1

while h<hm:
	h=h+t
	hm=hm+tm
	cont=cont+1
print(cont)
	