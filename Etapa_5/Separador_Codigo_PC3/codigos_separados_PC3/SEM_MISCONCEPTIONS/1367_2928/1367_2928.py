snowberry = float(input("Quantidade de Snowberry"))
salfogo= float(input("Quantidade de Sais de Fogo"))
amanita = float(input("Quantidade de Amanita"))

quantidade1 = snowberry//0.31
quantidade2 = salfogo//0.73
quantidade3 = amanita//2.64

pocoes = min(quantidade1,quantidade2,quantidade3)

print(pocoes)