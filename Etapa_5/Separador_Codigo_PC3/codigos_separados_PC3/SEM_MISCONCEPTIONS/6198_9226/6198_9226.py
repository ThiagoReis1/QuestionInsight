altura_luna = 1.65
taxa_crescimento = 0.02

pessoa_altura = float(input("digite a altura: "))
pessoa_crescimento = float(input("digite a altura: "))
ano = 0 

while altura_luna > pessoa_altura:
	pessoa_altura = pessoa_altura + pessoa_crescimento 
	altura_luna = altura_luna + taxa_crescimento
	ano = ano + 1
print(ano)