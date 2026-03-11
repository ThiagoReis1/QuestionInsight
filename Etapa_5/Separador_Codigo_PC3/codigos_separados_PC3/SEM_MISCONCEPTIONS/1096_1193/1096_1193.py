numero = float(input("numero: "))
formula = (numero // 10000)**3 + (numero % 10000)**3 + (numero // 10000)**3
if (numero == formula):
    print("X atende a propriedade")
else:
    print(formula)