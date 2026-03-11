def preco_estacionamento(t: float) -> float:
	total = 5.00
	if (t < 2.0):
		total += 1.25
	elif (t == 2.0):
		total += 2.25
	else:
		total += 3.25
	
	print(round(total, 2))
	
if __name__ == "__main__":
	tempo = float(input(""))
	preco_estacionamento(tempo)