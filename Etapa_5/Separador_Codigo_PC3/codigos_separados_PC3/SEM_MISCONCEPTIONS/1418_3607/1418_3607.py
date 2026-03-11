maisV = int(input())
seg = int(input())
menosV = int(input())

total = maisV + seg + menosV

if maisV > (total/2):
	print("NAO")
else:
	print("SIM")