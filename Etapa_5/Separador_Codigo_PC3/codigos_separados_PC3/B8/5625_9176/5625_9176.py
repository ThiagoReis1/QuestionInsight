escolha = input("Digite (T) para Tapioca ou (S) para Salgado: ")
qtde_escolha = int(input("Digite a quantidade: "))
acai = int(input("Digite a quantidade de acais: "))
escolha = escolha.upper()
acai = acai * 10
if escolha == "T":
 total = qtde_escolha * 5.5 + acai
elif escolha == "S":
 total = qtde_escolha * 4 + acai
print(round(float(total), 1))
 
