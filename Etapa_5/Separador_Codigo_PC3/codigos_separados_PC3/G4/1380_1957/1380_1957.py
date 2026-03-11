ec = float(input("estimativa_de_carro_por_metro_quadrado: "))
b = float(input("comprimento_base_maior: "))
B = float(input("comprimento base maior: "))
h = float(input("comprimento_altura: "))


A = ( h*(B + b)/2)
QC = ec*A
print(int(round(QC,2))) 