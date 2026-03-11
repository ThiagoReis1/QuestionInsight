A=80
B=50
C=30
quantidadeA=float(input("Bilhetes vendidos da classe A?:"))
quantidadeB=float(input("Bilhetes vendidos da calsse B?:"))
quantidadeC=float(input("Bilhetes vendidos da classe C?:"))
rendaTotal=quantidadeA * A + quantidadeB * B + quantidadeC * C
print(round(rendaTotal, 2))