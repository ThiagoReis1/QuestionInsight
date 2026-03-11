
peso = float(input("peso_gramas:")) 
qntd = float(input("qntd_gramas:"))

perdido =  qntd * 5
rest_saco = peso - perdido

print(round(rest_saco,2))
