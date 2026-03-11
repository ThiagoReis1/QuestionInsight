a = float(input("primeira nota: "))
b = float(input("segunda nota: "))
c = float(input("terceira nota: "))

x = (a + b + c)/3

if(x >= 6.0):
	print(round(x, 2))	
	print("Aprovacao")
else:
	print(round(x, 2))
	print("Reprovacao")
   
	

					