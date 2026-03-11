largura= float(input("Qual a largura da fazenda? "))
comprimento= float(input("Qual o comprimento da fazenda? "))
custo= float(input("Qual o custo da construcaoo por metro? "))

perimetro= 2* (largura + comprimento)
custo_total= perimetro * custo

print(round(custo_total, 2))

