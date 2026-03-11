# faça seu código aqui!
frase = input("Coloque a frase: ")
frase = frase.upper()

contador_d = 0
i = 0 
tamanho = len(frase)
while i < tamanho:
   if frase[i] == "D":
      contador_d += 1
   i += 1
print(contador_d)