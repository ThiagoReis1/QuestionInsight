#leitura 
capital = float(input("valor da compra "))
tempo = int(input("quantidades de parcelas "))

#processamento
juros = capital*(0.03)*tempo

m = capital + juros 

print(float(m))
