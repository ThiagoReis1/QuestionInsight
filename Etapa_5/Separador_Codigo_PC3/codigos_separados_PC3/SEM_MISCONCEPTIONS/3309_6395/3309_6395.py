peso = float(input(" Digite o peso da mercadoria a ser transportada em kg "))


kg = 43.21
taxa_fixa = 25
ICMS = 0.62

frete =  ((peso * kg)  + taxa_fixa ) 
total = frete * ICMS + frete

print(round(total, 2))

