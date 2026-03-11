from numpy import *
m = array(eval(input("matriz: ")))
media = (sum(m) - min(m))/(size(m)-1)
print(round(media,2))