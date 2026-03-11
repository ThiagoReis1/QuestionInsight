N = int(input("Insira um numero inteiro maior ou igual a 1: "))

if N >= 1 and (N % 3 == 0) and not(N % 5 == 0):
	print("Plunct")
elif N >= 1 and (N % 5 == 0) and not(N % 3 == 0):
	print("Plact")
elif N >= 1 and (N % 3 == 0) and (N % 5 == 0):
	print("Zuuum")
else:
	print(N)
