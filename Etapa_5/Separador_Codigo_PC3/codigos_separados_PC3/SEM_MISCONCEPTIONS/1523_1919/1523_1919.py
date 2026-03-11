inicio = int(input("Quantidade inicial: "))
quant_c = int(input("Quantidade C de balões: "))
quant_d = int(input("Quantidade D de balões: "))
baloes = 200
t = 0
while(inicio<200):
	baloes = baloes - (quant_c - quant_d)
	t = t + 1
print(t)