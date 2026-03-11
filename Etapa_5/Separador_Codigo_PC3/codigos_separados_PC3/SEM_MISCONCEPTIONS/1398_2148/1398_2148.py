tempo = float(input("insira o tempo: "))
valor1 = (100 * tempo) + 5000
valor2 = 8000 + 100 * 20 + 90*tempo

if(tempo <= 200):
	print(valor1)

else:
	print(valor2)