chifre_encantamento = 4;
ouro_encantamento = 3.14;
oleo_encantamento = 10;

chifre = float(input ("quantidade de chifre de touro:"))
ouro = float(input("quantidade de ouro em po:"))
oleo = float(input("quantidade de oleo de dwarven:"))

chifre1 = chifre/chifre_encantamento
ouro1 = ouro/ouro_encantamento
oleo1 = oleo/oleo_encantamento

razao = min(chifre1,ouro1,oleo1)

print(int(razao))
