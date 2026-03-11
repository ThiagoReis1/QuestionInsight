dias = int(input("informe a quantidade de dias: "))

if dias < 15:
	t = (dias * 175) + 20
elif dias == 15:
	t = (dias * 175) + 16
else:
	t = (dias *175) + 10
	
print(round(t, 2))