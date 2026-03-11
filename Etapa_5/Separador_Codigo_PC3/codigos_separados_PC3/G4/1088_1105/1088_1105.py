A = float(input("nota A: "))	
B = float(input("nota B: "))
C = float(input("nota C: "))
D = float(input("nota D: "))
E = float(input("nota E: "))
media = (A + B + C + D + E)/ 5
if (media >= 7):
	print(round(media,2))
	print("Aprovacao")
else:
	print(round(media,2))
	print("Reprovacao")