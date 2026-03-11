x = float(input("digite o valor de x: "))

if (x <=  -1 or x >= 1):
	cont = x  
elif(-1 < x < 0 or 0 < x < 1 ):
      cont = 1
elif( x == 0):
	cont = 2
print(round(cont, 2))