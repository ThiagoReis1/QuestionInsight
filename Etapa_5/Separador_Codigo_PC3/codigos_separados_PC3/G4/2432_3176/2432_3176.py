pa = float(input("preco por metro quadrada:"))
ap = float(input("area privativa metro quadrado:"))
ac = float(input("area comum metro quadrado:"))
ag = float(input("area garagem metro quadrado:"))

pt = ((ap+ac+ag)*pa)

print(round(pt,2))