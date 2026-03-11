v = float(input("Digite o volume total consumido no mes: "))
C1 = ((0.37 * v) + 15) 
C2 = C1*(35/100)
C3 = C1 + C2
print(round(C3, 2))
