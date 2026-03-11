volume_de_agua = float(input("qual o volume de agua consumida? "))

consumo = (volume_de_agua * 0.37) + 15.0

ICMS = (consumo * 35.0) / 100.0

total = consumo + ICMS

print(round(total, 2))