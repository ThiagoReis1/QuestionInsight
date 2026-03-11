precoArea = float(input())
areaPrivativa = float(input())
areaComum = float(input())
areaGaragem = float(input())

precoTotal = ((areaPrivativa + areaComum + areaGaragem) * precoArea)

print(round(precoTotal, 1))