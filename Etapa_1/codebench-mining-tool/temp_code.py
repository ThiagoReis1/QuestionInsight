numero = int(input("Digite um numero inteiro: "))

# Print even numbers up to 'numero'
for i in range(0, numero + 1, 2):
    print(i, end=" ")

print()  # Move to the next line after printing even numbers

# Print numbers in reverse order from 'numero' to 0
for i in range(numero, -1, -1):
    print(i, end=" ")