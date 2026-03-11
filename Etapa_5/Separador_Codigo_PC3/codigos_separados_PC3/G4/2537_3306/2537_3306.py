v= float(input("digite o valor da heranca:"))
m= float(input("digite o saque mensal:"))
j= float(input("digite o juros:"))
saldo= v 
t=0
if(v>0 and m>0 and j>0):
	while(saldo<=(1.2*v)):
		saldo= saldo +(saldo*(j/100))
		saldo= round(saldo, 2)
		saldo= saldo - m	
		t= t+1
	print(t)

else:
	print("Dados incorretos")
		
