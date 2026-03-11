#entrada de dados
l=float(input("Digite a largura da fazenda: "))
c=float(input("Digite o comprimento da fazenda: "))
v= float(input("Digite o custo de construcao da cerca por metro: "))
custo= (2*(l+c))*v
print(round(custo,2))