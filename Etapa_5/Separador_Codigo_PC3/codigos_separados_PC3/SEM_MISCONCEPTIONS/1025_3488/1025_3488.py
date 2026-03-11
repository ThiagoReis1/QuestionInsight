valor1 = float(input("largura em m: "))
valor2 = float(input("comprimento em m: "))
valor3 = float(input("custo da construcao por m: "))

perimetro = 2 * (valor1 + valor2)

t = valor3 * perimetro

print(round(t, 2))