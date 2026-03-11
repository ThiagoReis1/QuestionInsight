# faça seu código aqui!

x = int(input("Dias reservados:"))
diaria = 175

if x < 15:
	y = diaria*x + 20
elif x == 15:
	y = diaria*x + 16
elif x > 15:
	y = diaria*x + 10
	
print(round(y,2))