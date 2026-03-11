largura = float(input("largura: "))
comprimento = float(input("comprimento: "))
custo = float(input("custo do trabalho: "))
A = largura
a = comprimento

perimetro = 2 * (A + a)

custototal = perimetro * custo

print(round(custototal,2))