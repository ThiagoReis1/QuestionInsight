n = float(input("quantidade de combustivel comum"))
if (n < 17.5) :
	print(round(n + 1.5 , 1))
elif( n >= 17.5) and (n < 35.0):
	print(round(n + 2.3 , 1))
elif (n >= 35.0) and (n < 50.0):
	print(round(n + 3.3 , 1))
elif (n >= 50.0):
	print(round(n + 4.7 , 1))
