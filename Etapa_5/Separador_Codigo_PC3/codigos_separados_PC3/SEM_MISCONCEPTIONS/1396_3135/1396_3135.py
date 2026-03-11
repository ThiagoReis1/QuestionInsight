conta=float(input("Insira a conta:"))

p1 =conta /10
p2 =conta *0.06

caso1= conta + p1
caso2= conta + p2

if (conta<=300):
	print(round(caso1,2))
else:
	print(round(caso2,2))