v = float(input("valor do premio: "))
a = (1.2*v)
m = float(input("saque mensal: "))
j = float(input("juros: "))/100
t = 0
s = 0
if (v>0 and m>0  and j>0):
	while (s <= a):
		s = round(s + ((v-m) + j*(v-m)) , 2)
		t = t + 1		
else:
	print("Dados incorretos")
	
print(t)
