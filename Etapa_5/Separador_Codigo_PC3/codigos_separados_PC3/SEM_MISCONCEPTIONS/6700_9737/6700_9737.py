dias_uso = int(input("Dias de uso: "))

valor_t = (dias_uso*50)+30
icms = valor_t+valor_t*(18/100)
print(round(icms,2))