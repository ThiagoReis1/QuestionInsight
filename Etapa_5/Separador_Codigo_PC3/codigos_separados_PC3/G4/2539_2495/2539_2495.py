v = float(input("valor do premio: "))
m = float(input("saque mensal: "))
j = float(input("taxa de juros: "))
if(v>0 and m>0 and j>0):
	s = 0
	t = 0
	while(s*0.2<=v):
		s = s + (v*j-m)  
		t = t+1
	print(round(t,2))
else:
	print("dados incorretos")