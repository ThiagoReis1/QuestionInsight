a=float(input("Valor de a:"))
b=float(input("valor de b:"))
c=float(input("valor de c:"))
custo_servico=float(input("qual o custo do serviço?"))
perimetro=a+b+c
custo_total=perimetro*custo_servico
print(round(custo_total, 2))