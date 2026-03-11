nome = input("Digite um nome: ")

# Verifique se o nome tem pelo menos 4 caracteres
if len(nome) >= 4:
    # Verifique se a quarta letra é 'i' (maiúscula ou minúscula)
   if nome[3].lower() == 'i':
        # Se sim, imprima o nome em letras maiúsculas
      print(nome.upper())
   else:
        # Caso contrário, imprima "nome inválido"
      print("Nome inválido")
   else:
    # Se o nome tiver menos de 4 caracteres, imprima "nome inválido"
     print("Nome inválido")