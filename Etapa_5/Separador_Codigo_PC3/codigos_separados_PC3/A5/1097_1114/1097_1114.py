import math
X = int(input("Digite um número: "));
x1 = X // 100000
rest_x1 = X % 100000
x2 = rest_x1 // 10000
rest_x2 = rest_x1 % 10000
x3 = rest_x2 // 1000
rest_x3 = rest_x2 % 1000
x4 = rest_x3 // 100
rest_x4 = rest_x3 % 100
x5 = rest_x4 // 10
rest_x5 = rest_x4 % 10
x6 = rest_x5 // 1
y = x1 * 100 + x2 * 10 + x3 * 1;
z = x4 * 100 + x5 * 10 + x6 * 1;
if(X == (y - z) ** 2 ):
	print(X, "atende a propriedade");
else:
	a = (y - z) ** 2
	print(a);