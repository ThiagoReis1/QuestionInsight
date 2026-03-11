dias = float(input("Coloque os dias: "))

vr1 = dias * 50 + 30
icms = 0.18

total = vr1 * icms + vr1

print(round(total, 2))