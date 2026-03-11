preco  = from(input("Preco: "))
altura = from(input("Altura: "))
raio   = from(input("Raio: "))
volume = pi * raio**2 * altura
total = preco * volume
print(round(total, 2))