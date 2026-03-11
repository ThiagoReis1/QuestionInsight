hf=float(input())
tf=float(input())
hm = 1.86
tm = 0.01
cont=0
while hf<hm:
	hf=(hf+tf)
	hm=hm+tm
	cont=cont+1
print(cont)