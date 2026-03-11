from numpy import*
a = array(eval(input("Insira as notas: ")))
med = (sum(a) - min(a))/(size(a) - 1)
print(round(med,2))
