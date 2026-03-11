nmilho = int(input("Quantos milhos?"))

if nmilho < 6:
	precomilho = 1.85
	preco_total = precomilho * nmilho
	
else:
	precomilho = 1.5
	preco_total = precomilho *nmilho

print(round(preco_total,2))
