d=float(input())
tf=float(input())
j=float(input())
cont=0
inicial=d

if d > 0 and tf > 0 and j > 0:
	while inicial > (tf*(tf*0.1)):
		d=round(d+(d*(tf/100)-tf),2)
		cont=cont+1
		tf=float(input())
else:
	print("Dados incorretos")
		
		