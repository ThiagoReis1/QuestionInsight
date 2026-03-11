
#estimativa de acaizeiros:
estimativa = float(input("estimativa: "))


#comprimento de aresta do campo:
aresta = float(input("aresta: "))


#q total de acaizeiros no campo:
total = (3/2) * (3 * (aresta)**2)**0.5
estimativa_total = int(estimativa * total)
print(estimativa_total)
