e = input("escolha lanche(L) ou prato (P):")
q = int(input("Digite a quantidade:"))
r = int(input("Digite a quantidade de refrigerante:"))
 
l = 6
p = 13.50

if e==("L"):
   c = (l*q) + (r*3)
   print(round(c,2))
else: 
   k = (p*q) + (r*3)
   print(round(k,2))
 