x = float(input("x: "))

f_x = 0

if (x >= -1000 and x< -2):
	f_x = -1/(x+2)
	f_x = round(f_x,4)
elif(x > 2 and x <= 1000):
	f_x = 1/(x-2)
	f_x = round(f_x,4)
else:
	f_x = "entrada invalida"
print(f_x)