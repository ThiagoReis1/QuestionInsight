altura_max = 1.75
cres_max = 0.01
altura_m = float(input(" "))
cres_m = float(input(" "))
ano = 0

while altura_m < altura_max:
	altura_max += cres_max
	altura_m += cres_m
	ano += 1
print(ano)
	
	


