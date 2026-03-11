fixo = 45.00
acre = 0.97
icms = (42/100)+1

minutos = float(input("quantidade de minutos excedentes: "))


total = ((acre*minutos)+fixo)*icms


print(round(total, 2))