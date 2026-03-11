minutos = float(input("quantos minutos ficou ? : "))
assinatura = 23.00
plano = 0.28 * minutos + assinatura
ICMS = (plano * 31) / 100
consumo_total = plano + ICMS
print(round(consumo_total, 2))