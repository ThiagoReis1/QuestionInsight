
a = float(input("qual o comprimento do  terreno em metros ? : "))
b = float(input("qual a largura do terreno em metros ? : "))
c = float(input("qual a altura do terreno em metros ? : "))
quanto_gastar = float(input("quando quer gastar por metro ? :"))
custo = (a + b + c) * quanto_gastar
print(round(custo, 2))