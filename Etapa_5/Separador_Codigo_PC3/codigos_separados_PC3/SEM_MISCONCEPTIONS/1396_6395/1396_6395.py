consumo = float(input("Digite o valor consumido no reustaurante: "))

if(consumo <= 300):
	gorjeta1 = consumo * 0.10
	v_total = consumo + gorjeta1
	
else:
	gorjeta2 = consumo * 0.06
	v_total = consumo + gorjeta2
print(round(v_total, 2))
	