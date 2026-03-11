velo = int(input("digite a velocidade: "))

if velo < 10:
	total = 50.00 + 5.50
elif velo == 10:
	total = 50.00 + 7.75
else:
	total = 50.00 + 10.00
print(round(total, 2 ))
	
