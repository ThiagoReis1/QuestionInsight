plano = 45
me = float(input("insira um valor: "))
total = plano + me * 0.97
icms = total * 42/100
pagar = total + icms
print(round(pagar, 2))
								