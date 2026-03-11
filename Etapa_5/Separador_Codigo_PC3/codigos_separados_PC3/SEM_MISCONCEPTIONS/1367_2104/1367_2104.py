snowberry = float(input("quantidade de snowberry:"))
sais = float(input("sais de fogo:"))
amanita = float(input("amanita:"))

pso = (snowberry/0.31)
psa = (sais/0.73)
pam = (amanita/2.64)

porcoes = int(min(pso,psa,pam))
print(porcoes)