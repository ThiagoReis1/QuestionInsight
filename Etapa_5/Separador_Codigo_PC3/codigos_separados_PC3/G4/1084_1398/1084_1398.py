A = float(input("nota A: "))
B = float(input("nota B: "))
C = float(input("nota C: "))
D = float(input("nota D: "))
m = ((A+B+C+D)/4)
print(round(m, 1))

if (m>= 6):
 print("Aprovado")
else :
 print("Reprovado")