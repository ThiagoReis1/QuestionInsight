num = float(input("Tempo de voo em minutos: "))
num2 = num - 200
x = (8000 + 100 * 200) + 90*num2
y = 5000 + 100 * num 


if num >= 200:
	print(x)
else:
	print(y)