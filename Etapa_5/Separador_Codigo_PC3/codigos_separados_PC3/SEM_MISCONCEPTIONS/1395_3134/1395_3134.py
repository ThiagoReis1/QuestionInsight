conta=float(input("insira a conta:"))

p1= conta/0.5
p2= conta/10

caso1= conta / p1
caso2= conta / p2

if (conta>=1000):
	print(round(caso1,2))
else:
	print(round (caso2,2))
