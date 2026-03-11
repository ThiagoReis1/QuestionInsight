# Universidade Federal do Amazonas
# Aluna: Karina Rocha Ferreira - 21554907
# Avaliacao 2. 29/06/2016

x = int(input())

d = x // 1000
resto_d = x % 1000

form = (d + resto_d)**2

if(x == form):
	print(form, "atende a propriedade")
else:
	print(form)