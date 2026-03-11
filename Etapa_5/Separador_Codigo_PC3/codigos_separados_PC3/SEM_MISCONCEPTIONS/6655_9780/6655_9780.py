from numpy import*
notas=array(eval(input("coloque as 2 notas: ")))
peso= array([5,1])
num= notas* peso
media=sum(num)/ sum(peso)
print(round(media,2))