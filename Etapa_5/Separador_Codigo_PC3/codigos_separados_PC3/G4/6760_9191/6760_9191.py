# faça seu código aqui!
Q=int(input("quantidade de pecas:"))

if Q<10:
	x=30+3.25
	
elif Q==10:
	x=30+4.50
	
else:
	x=30+6.00
	
print(round(x,2))