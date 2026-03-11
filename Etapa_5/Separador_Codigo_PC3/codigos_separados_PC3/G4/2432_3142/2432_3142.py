PA = float(input("Preco da area por m2: "))
AP = int(input("Area privativa por m2: "))
AC = int(input("Area comum por m2: "))
AG = int(input("Area da garagem por m2: "))

TOTAL = ((AP + AC + AG) * PA)

print(float(round(TOTAL , 2)))