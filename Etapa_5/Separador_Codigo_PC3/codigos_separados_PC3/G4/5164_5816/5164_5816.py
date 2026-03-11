#determinar as entradas
p = float(input("Quantas gramas ha em um saco de racao? ")) 
q = float(input("Qual a quantidade em gramas usada diariamente? "))
f = p - ( q * 4 )
print(round(f,2))