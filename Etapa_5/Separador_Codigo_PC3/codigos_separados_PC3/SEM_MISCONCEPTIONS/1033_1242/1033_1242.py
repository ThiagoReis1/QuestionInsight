int(input("Peso da mercadoria em kg :"))
quilo = 43.21 
taxa_fixa = 25.00
total = ((quilo + taxa_fixa)* 10) 
resto = total % 62
print(round(resto,2))
