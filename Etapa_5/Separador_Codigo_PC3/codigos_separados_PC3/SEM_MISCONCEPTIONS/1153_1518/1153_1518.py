# universidade federal do amazonas
# aluno : geovanni vieira - 21453456

bp = float(input("digite o patrimonio do banco pobresco:"))
bit = float(input("digite o patrmonio do bitcoin:"))
cresanual = float(input(" percentual de crescimento liquido anual do pobresco:"))
cresanual2 = float(input("o percentual de crescimento liquido anual do bitcoin:"))

i = 0
soma = 0

while i <= bp:
	soma = bit * cresanual2/100 - cresanual/100
	i = i + 1
   print(soma)

