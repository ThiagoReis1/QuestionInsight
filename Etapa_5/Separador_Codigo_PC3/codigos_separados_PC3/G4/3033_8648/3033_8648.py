#variáveis de enteada:
x = float(input("Digite valores quais x pode assumir: "))
#Condições e cálculo:
if (-100 <= x < 0):
 f = (-1 / x)
 print(round(f, 4))
elif (0 < x <= 100):
 f = (1 / x)
 print(round(f, 4))
else:
 print("entrada invalida")