c=float(input())
d=float(input())
m=float(input())
j=float(input())
cp=d
j=j/100
t=1
saldo=(c*j)- d
if(c>0 and d>0 and m>0 and j>0):
	while(saldo<=t):
		
	print(round(t,2))

else:
	print("Dados incorretos")
	
print(round(t,2))