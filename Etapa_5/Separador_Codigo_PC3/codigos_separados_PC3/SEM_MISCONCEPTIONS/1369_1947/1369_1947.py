#----------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# VICTOR ALEXANDRE GOMES WEIL - 21603648
# DATA: 27/10/2016
#
#
#----------------------------------
#Variaveis a seguir serao o material necessario para realizar o encantamento
flawless_ruby=4.0
soul_gem=3.14
dwarven=10.0
flawless_ruby_disponivel=float(input("Flawless ruby disponivel na cidade:"))
soul_gem_disponivel=float(input("Soul gem disponivel:"))
oleo_dwarven_disponivel=float(input("Oleo de dwarven disponivel:"))
encantamento=min(flawless_ruby_disponivel//flawless_ruby, soul_gem_disponivel // soul_gem, oleo_dwarven_disponivel // dwarven)
print(encantamento)

#A variavel encantamento vai pegar o menor valor inteiro disponivel entre as variaveis para deduzir a qtd de encantamentos possiveis de ser produz