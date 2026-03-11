consumo = float(input("Qual foi o consumo de chamadas (minutos)?"))
consumototal = (consumo*0.28)+23
imposto = consumototal*0.31
soma = imposto+consumototal

print (round(soma,2))