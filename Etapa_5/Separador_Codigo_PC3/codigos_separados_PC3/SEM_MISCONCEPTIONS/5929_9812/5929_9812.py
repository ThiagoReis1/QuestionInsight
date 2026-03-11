# conta_agua

volume = float(input("Digite o volume de agua consumido: "))

conta_agua = (volume * 0.37) + 15

total = conta_agua * 0.35 + conta_agua

print(round(total,2))