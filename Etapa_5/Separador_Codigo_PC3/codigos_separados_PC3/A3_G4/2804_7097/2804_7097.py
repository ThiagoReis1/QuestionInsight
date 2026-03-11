dp=float(input("qual o valor inicial?"))
meses=int(input("quantos meses"))
m=0
j=1/100
while meses>0:
	meses=meses-1
	dp=(dp*j)+dp
	print(round(dp,2))