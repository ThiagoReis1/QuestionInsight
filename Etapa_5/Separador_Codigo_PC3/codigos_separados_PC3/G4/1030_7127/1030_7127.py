m = float(input("minutos excedentes: "))
Tm = 0.97*m
T = Tm+Tm*0.42
V = 45*0.42+45+T
print(round(V,2))