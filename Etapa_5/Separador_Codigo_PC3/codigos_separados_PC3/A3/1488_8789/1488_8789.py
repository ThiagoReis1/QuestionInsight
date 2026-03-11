m=int(input())

if m>=0 and m<=100:
	valor=m*1.20+1
if m>100 and m<=200:
	valor=m*1.30+10
if m>200 and m<=300:
	valor = m*1.40+20
if m>300:
	valor=m*1.50+25

print(round(valor,2))