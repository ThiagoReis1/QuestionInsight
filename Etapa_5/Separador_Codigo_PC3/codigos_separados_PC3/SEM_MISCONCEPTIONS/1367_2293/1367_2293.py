snowberry = float(input("quantidade de snoweberry: "))
sais_de_fogo = float(input("quantidade de sais de fogo: "))
amanita = float(input("quantidade de amanita: "))

pocao = (0.31 + 0.73 + 2.64)
qmax = (snowberry / 0.31 + sais_de_fogo / 0.73 + amanita / 2.64) / pocao

print(int(qmax / min(snowberry / 0.31,sais_de_fogo / 0.73,amanita / 2.64)))