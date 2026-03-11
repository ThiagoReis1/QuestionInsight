quantidade = float(input("minutos excedentes: "))
mes = (quantidade * 0.97 +  45) 
imposto = mes * (42/100)
total = mes + imposto 
print(round(total, 2))