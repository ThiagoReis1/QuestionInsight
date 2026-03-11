a= float(input("notas: "))
b= float(input("notas: "))
c= float(input("notas: "))
d= float(input("notas: "))
ma = ((a + b+c+d)/4)
print(round(ma,2))
if(ma>=5):
	print("Aprovacao")
else:
	print("Reprovacao")