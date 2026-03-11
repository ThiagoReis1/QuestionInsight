from math import*

EA = float(input("Estimativa de árvores por metro quadrado:"))
CL = float(input("Comprimento do lado da região pentagonal de floresta:"))

AP = (CL**2 * sqrt(25+10 * sqrt(5)))/4

AT = EA * AP

print(int(round(AT,2)))