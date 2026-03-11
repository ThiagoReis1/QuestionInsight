v= float(input("valor do premio: "))
m= float(input("valor do saque mensal: "))
j= float(input("taxa de juros:"))

meses=0
s=v
quero= (20*v)/100 + v
#if(v<=0 or m<=0 or j<=0):
#	print("Dados incorretos")
#else:
while(s<quero):
	s= s+ (v*j)/100 -m 
	s= round(s,2)
	meses= meses+1
	
print(meses)	