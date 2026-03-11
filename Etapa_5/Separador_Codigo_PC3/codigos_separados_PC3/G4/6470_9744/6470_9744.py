import math
lado = float(input("escreva valor"))
tan = float(math.tan((math.pi)/7))
apot = float(lado/(2*tan))
area = float((7*lado*apot)/2)
print(round(area, 2))