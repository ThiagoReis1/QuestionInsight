from numpy import*
vet = array(eval(input("")))
media = (sum(vet)-min(vet))/(size(vet)-1)
print(round(media,2))