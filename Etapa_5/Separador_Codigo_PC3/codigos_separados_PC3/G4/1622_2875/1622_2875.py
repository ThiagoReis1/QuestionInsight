from numpy import*
ent= array(eval(input("Quantidade de pessoas que entraram no ônibus: ")))
sai= array(eval(input("Quantidade de pessoas que sairam no ônibus: ")))
j= sum(ent)
w= sum(sai)
total= j-w
print(total)