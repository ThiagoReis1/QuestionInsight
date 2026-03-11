def main():
    # Solicita ao usuário um número inteiro positivo N
   n = int(input("Digite um número inteiro positivo: "))

    # Verifica se o número fornecido é positivo
   if n <= 0:
        print("Por favor, digite um número inteiro positivo.")
      return

    # Realiza a contagem regressiva de N até 2
   print("Contagem regressiva iniciada:")
    for i in range(n, 1, -1):
      print(i)

    # Exibe a mensagem de fim da contagem regressiva
    print("Fim da contagem regressiva!")

if __name__ == "__main__":
    main()