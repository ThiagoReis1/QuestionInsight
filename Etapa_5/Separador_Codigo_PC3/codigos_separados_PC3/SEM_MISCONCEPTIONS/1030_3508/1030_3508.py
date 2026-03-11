me = float(input("minutos excedentes: "))
plan1 = (me * 0.97 + 45)
imposto = plan1 * 42/100
print(round(imposto + plan1 ,2))