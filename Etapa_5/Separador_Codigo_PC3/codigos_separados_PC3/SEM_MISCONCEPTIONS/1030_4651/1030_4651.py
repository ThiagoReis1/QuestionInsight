m=float(input("Digite a quantidade de minutos excedentes: "))

total_mensal=45+(m*0.97)
total_imp=total_mensal*0.42

total=total_mensal+total_imp

print(round(total,2))