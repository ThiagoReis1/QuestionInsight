qfrnec = 4.0
qsgnec = 3.14
qodnec = 10

qfr = int(input('Insira a quantidade de Flawless Ruby disponível, em gramas: '))
qsg = float(input('Insira a quantidade de Soul Gem disponível, em gramas: '))
qod = int(input('Insira a quantidade de Óleo de Dwarven disponível, em gramas: '))
ban1 = (qfr + qsg + qod)

mi = print(min(qfr, qsg, qod))
ma = print(max(qfr, qsg, qod))

qmax = 