from numpy import*
notas = array(eval(input("notas: ")))

media = [2,1,5]
media1 = sum(media)

media2 = notas * media

media3 = sum(media2) / media1 

print(round(media3, 2))
