peso=float(input())
distancia=float(input())
valor=peso*25+distancia*0.10
valor_total=valor+(valor*12/100)
print(round(valor_total,2))