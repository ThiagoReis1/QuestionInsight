snowberry = float(input("Quantidade de snowberry: "))
saisDeFogo = float(input("Quantidade de sais de fogo: "))
amanita = float(input("Quantidade de amanita: "))

pocaoSnowberry = int(snowberry / 0.31)
pocaoSaisDeFogo = int(saisDeFogo / 0.73)
pocaoAmanita = int(amanita / 2.64)

qtdePocao = min(pocaoSnowberry, pocaoSaisDeFogo, pocaoAmanita)

print (qtdePocao)