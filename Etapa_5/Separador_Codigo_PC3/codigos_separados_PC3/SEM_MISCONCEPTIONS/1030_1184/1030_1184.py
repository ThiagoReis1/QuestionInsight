minutos_exc = float(input("quantos minutos excederam:"))

valor_min_exc = minutos_exc * 0.97

conta_cel = ((45 + valor_min_exc) * 0.42) + 45 + valor_min_exc

print(round(conta_cel, 2))
