from numpy import*

v1 = array(eval(input("TEMPOS : ")))
v2 = array(eval(input("PERCENTUAL : ")))/100

litros =  v1*v2
agua = litros * 5

print(sum(agua))