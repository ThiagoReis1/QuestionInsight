# Entrada de dados e
definicao de constantes
q = 20000
juros = 12
saldo = q
# Tempo inicial
t = 1
# Atualizacao de saldo
while
(t <= 5):
rend = saldo * juros/100
saldo = saldo + rend
t = t + 1
# Exibicao de resultados
print
("Saldo: R$",
round
(saldo, 2))