s = float(input("quantidade de snowberry: "))
f = float(input("quantidade de sais de fogo: "))
a = float(input("quantidade de amanita: "))

fim = min((s/0.31),(f/0.73),(a/2.64))
print(int(fim))