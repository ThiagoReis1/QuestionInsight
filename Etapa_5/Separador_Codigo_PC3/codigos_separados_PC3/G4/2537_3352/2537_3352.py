v= float(input("valor da heranca:"))
s= float(input("saque mensal:"))
j= float(input("taxa de juros:"))/100

t=0
p= v+(v*20/100)

if(v>0 and s>0 and j>0):
	while(p>v):
		v=v+j*v-s
		v=round(v,2)
		t=t+1
	print(t)	
else:
	print("Dados incorretos")
