def aplicar_codigo_secreto(mensagem):
    codigo_secreto = []

    # Percorre cada número na mensagem
    for num in mensagem:
        # Se o número for 9, substitui por 0
        if num == 9:
            codigo_secreto.append(0)
        # Para os demais números, aplica a transformação
        else:
            codigo_secreto.append((num + 1) ** 2)

   return codigo_secreto

def main():
    # Solicita ao usuário a entrada da mensagem como uma lista de números
   mensagem = list(map(int, input("Digite a mensagem numérica: ").split()))

    # Aplica o código secreto na mensagem
   mensagem_codificada = aplicar_codigo_secreto(mensagem)

    # Exibe a mensagem codificada
   print("Mensagem codificada:", mensagem_codificada)

if __name__ == "__main__":
    main()