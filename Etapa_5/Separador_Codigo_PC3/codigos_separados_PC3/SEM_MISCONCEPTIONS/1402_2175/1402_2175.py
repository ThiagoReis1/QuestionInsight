nome_da_arma  = (input("Digite o nome da arma: "))
fator_de_sucesso= int(input("Digite o numero: "))
if int(1 <= fator_de_sucesso <= 10):
machado = int(30 * fator_de_sucesso / 10)
print(machado)
lanca = int(5 + 20 * fator_de_sucesso/10)
print(lanca)