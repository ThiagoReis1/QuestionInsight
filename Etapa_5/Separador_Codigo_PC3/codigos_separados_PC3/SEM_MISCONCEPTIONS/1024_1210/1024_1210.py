# Universidade Federal do Amazonas
# Aluno: Philippe da Silva Soares
# Matrícula: 21650892
# Objetivo: Escrever um programa que informe o custo total da construção de uma cerca.

# Lados do terreno(em metros)
a=float(input("informe o lado a: "))
b=float(input("informe o lado b: "))
c=float(input("informe o lado c: "))

# Custo da construção da cerca por metro
custo_por_m=float(input("informe o custo de construção da cerca por metro: "))

# Perímetro da roça
p=a+b+c

# Custo toal da construção da cerca
custo_total=(p*custo_por_m)

print(round(custo_total,2))





