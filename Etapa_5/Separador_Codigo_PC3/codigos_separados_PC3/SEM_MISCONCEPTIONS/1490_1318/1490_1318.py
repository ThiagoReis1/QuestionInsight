
def pagarConta():
	volume = float(input())
	if(volume >= 0.0 and volume <= 10.0):
		conta = (volume * 3.00) + 15.00
		return conta
	if(volume > 10.0 and volume <= 15.0):
		conta = (volume * 3.50) + 20.00
		return conta
	if(volume > 15.0 and volume <= 20.0):
		conta = (volume * 4.00) + 25.00
		return conta
	if(volume > 20.0):
		conta = (volume * 4.50) + 30.00
		return conta
	return 0

print(round(pagarConta(),2))