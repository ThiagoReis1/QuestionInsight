#Escreva um programa que leia:
#O peso do saco de ração em gramas.
ps = float(input("Peso do saco de racao em gramas:"))
#A quantidade de ração fornecida para cada porco em gramas.
qp = float(input("Quantidade re racao fornecida para cada porco em gramas:"))
#Cálculo:
t = ps - qp*5
print(round(t , 2))
