num = int(input("consumo de minutos de um cliente"))
mun = (num < 100)
mun2 = (num > 100)
var1 = (mun * 1,20)
var2 = (mun2 * 1,40) + 25,0
print(round(var2, 2))
print(round(var1, 2))