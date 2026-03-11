import math

var = float(input("Digite valor de veneno injetado: "))

qt_casca = (var/5)*(math.sqrt(9/5))
qt_alho = (var**2)/(math.pi)
qt_oleo = (math.sqrt(5*var/3))

print(round(qt_casca, 2))
print(round(qt_alho, 2))
print(round(qt_oleo, 2))