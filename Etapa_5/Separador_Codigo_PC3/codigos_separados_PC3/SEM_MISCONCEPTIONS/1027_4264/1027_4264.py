kwh = float(input("quantidade de kwh:"))
conta = (0.43*kwh)+10
imposto = conta*0.25
total = conta + imposto
print(round(total, 2))