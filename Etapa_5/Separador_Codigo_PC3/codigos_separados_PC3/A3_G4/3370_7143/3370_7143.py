u = input("Digite a unidade da medida: C para centimetro e P para polegada: ")
v = float(input("Digite o valor da medida: "))

if(v == "C"):
   C = 0.393701 * v
   print(round(C, 2))
else:
   P = v / 0.393701
   print(round(P, 2))