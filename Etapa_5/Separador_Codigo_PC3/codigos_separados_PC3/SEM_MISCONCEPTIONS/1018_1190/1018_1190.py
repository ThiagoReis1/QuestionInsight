catetoa=float(input("Digite o valor do cateto a:"))
catetob=float(input("Digite o valor do cateto b:"))
custo=float(input("Qual o valor do custo total do serviço por m2:"))

area=(catetoa*catetob)/2
valor=(area*custo)

print(round(valor,2))