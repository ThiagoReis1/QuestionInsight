CDT = float(input("Digite a quantidade disponível de chifre de touro: "))
O = float(input("Digite a quantidade disponível de ouro em pó: "))
OD = float(input("Digite a quantidade disponível de óleo de dwarven: "))

cdt = CDT // 4.0
o = O // 3.14
od = OD // 10.0

qtdm = min(cdt,o,od)

print(int(qtdm))




