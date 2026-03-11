quantia = int(input("quantia: "))

# numero de notas de 20
notas_6 = quantia // 6

# quantia que restou para o saque com notas menores que 20
resto_6 = quantia % 3

# numero de notas de 10
notas_3 = resto_6 // 3

print(int(notas_6))
print(int(notas_3))