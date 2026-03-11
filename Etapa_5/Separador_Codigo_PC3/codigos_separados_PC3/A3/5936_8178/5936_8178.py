kwh = 0.43
icms = (25/100)
taxa = 10.00

consumido = float(input())

sem_icms = consumido * kwh + taxa
com_icms = sem_icms * (25/100)

tentativa = sem_icms + com_icms

tudo = print(round(tentativa, 2))