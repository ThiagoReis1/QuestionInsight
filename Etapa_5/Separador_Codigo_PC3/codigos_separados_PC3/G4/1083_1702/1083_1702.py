p1 = float(input("Nota da p1"))
p2 = float(input("Nota da p2"))
p3 = float(input("Nota da p3"))
m = (p1+ p2+ p3)/3
print(round(m,2))
if(m>=6): 
	print("Aprovacao")
else:
	print("Reprovacao")
