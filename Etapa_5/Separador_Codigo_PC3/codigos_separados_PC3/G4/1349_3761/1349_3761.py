e = float(input("estimativa de arvores:"))
c = float(input("comprimento do lado:"))

area = ((c**2)*((25+10*(5**0.5))**0.5))/4
q = e*area
print(round(q, 0))