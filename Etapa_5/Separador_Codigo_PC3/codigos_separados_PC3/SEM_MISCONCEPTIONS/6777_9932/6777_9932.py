nascimento = int(input())
x = input().upper()
idade = 2023 - nascimento

if x != 'B' and x != 'I':
	print("invalido")
	
if x == 'B' and idade >= 18:
	ano = idade - 18
	print("sim")
	print(ano)
if x == 'B' and idade < 18:
	ano = 18 - idade
	print("nao")
	print(ano)
	
if x == 'I' and idade >= 17:
	ano = idade - 17
	print("sim")
if x == 'I' and idade < 17:
	ano = 17 - idade
	print("nao")
	print(ano)

