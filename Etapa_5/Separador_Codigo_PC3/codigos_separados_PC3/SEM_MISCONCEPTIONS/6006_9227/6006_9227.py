x = int(input("Numero de batatas compradas:"))
if(x >= 10):
	total = x*0.75

else:
	total = x*0.90
print(round(total, 2))