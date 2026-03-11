a = float(input("valor recebido "))
b = float(input("saque"))
c = float(input("taxa de juros "))

i = 0
t1 = a
if(a>0 and b>0 and c>0):
	while(t1 > a/2 ):
		t1 = t1 +(t1)*(c/100)-b
		t1 = round(t1,2)
		i = i + 1
	print(i)
else:
	print("Dados incorretos")










