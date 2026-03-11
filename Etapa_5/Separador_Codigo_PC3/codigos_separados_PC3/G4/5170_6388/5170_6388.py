P=float(input("peso do saco de racao em gramas:  "))
Q=float(input("quantidade diaria de racao:  "))

#temos 1 saco de ração
#temos 3 animais que alimentados todo dia com a ração
#a quantidade de ração é sempre a mesma
#OBJETIVO: determinar a quantidade de raçao que restará após 7 dias

R1= P - (Q * 7)

print(round(R1,3))