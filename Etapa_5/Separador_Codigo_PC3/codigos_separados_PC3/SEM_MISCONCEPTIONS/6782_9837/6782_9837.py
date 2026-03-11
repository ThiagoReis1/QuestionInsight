idade = int(input())
pais = input().upper()
ano = int(input())

min = 2023 - ano

if pais == "B":
	if idade >= "18":
print("sim")
  else:
print("nao")
 elif pais == "E":
	if idade >= "16":
print("sim")
 else:
print("nao") 
 else:
print("invalido")
