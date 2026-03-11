# Alimentação de pets

peso= float( input("Digite o peso do saco em gramas:"))
quantia= float( input( "Digite a quantidade fornecida ao pet:"))

calc= quantia *5
rest= peso - calc
print(round( rest, 3))
