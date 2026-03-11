qtde_dd = int(input("qtde: "))

var1 = qtde_dd * 32.90
desc1 = var1 - (var1 * 0.20)

if (qtde_dd > 3):
    print(round(desc1, 2))
else:
    print(round(var1, 2))
