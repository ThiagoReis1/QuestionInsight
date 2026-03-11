# menos que 6 (R$ 1.85)
# 6 ou mais (R$ 1.50)

nem = int(input("Digite o numero de espigas de milho compradas: "))

if (nem >= 6):
	total = nem * 1.50
	print(round(total,2))
	
else:
	total = nem * 1.85
	print(round(total,2))
	