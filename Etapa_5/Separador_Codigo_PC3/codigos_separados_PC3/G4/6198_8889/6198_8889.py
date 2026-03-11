a_g = float(input(""))
t_g = float(input(""))
#constantes
a_m = 1.65
t_m = 0.02 #var contadora anos = 0
anos = 0
# cada loop equivale a 1 ano
while a_g < a_m:
	a_g = a_g + t_g
	a_m = a_m + t_m
	anos += 1
# quantos anos levaria para ultrapassar a luna?
print(anos)


