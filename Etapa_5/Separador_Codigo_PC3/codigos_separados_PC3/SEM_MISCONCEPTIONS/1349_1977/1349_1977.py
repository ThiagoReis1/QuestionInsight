from math import*
estimativa = float(input())
a = float(input())
area = ((a**2) * sqrt(25+10*sqrt(5)))/4
qt_arvores = area * estimativa
print(int(round(qt_arvores,2)))