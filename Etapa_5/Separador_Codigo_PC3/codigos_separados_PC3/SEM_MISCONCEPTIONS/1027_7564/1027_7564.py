consu = float(input("Digite o valor: "))
custo = consu*0.43
fixo = custo+10
imposto = fixo*25/100
total= fixo+imposto

print(round(total,2))