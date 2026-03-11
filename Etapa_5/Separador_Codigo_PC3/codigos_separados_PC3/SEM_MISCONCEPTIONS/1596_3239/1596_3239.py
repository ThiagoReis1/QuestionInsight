from numpy import*
notas = array(eval(input("digite os valores: ")))
total = sum(notas)
menornota = min(notas) 
qnota = size(notas) - 1
media = (total - menornota) / qnota
print(round(media, 2))