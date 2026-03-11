import math
con_men = float(input("Informe a quantidade consumida por dia: "));
var = 0.37 * con_men + 15.00;
custo = var + (var * 35) / 100
print(round(custo,2));
