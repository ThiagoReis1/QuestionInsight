tempo_voo = float(input("tempo de voo:"))

x = (5000 + 100 * tempo_voo)
y = (8000 +(100 * 200) + 90 * (tempo_voo - 200) )

if(tempo_voo <= 200):
   mensagem = x
else:
   mensagem = y

print(round(mensagem,2))



