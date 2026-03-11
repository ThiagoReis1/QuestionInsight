from numpy import *
v = array(eval(input("Notas: ")))

x = (sum(v)-min(v))
y = (size(v)-1)
media = x/y

print(round(media, 2))