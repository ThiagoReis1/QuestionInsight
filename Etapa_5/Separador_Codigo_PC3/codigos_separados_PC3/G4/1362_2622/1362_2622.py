from math import sqrt
from math import pi

a = float(input());

casca = float((a/5)*sqrt(9/5));
alho = float((a*a)/pi);
oleo = float(sqrt((5*a)/3));

print("%.2f" % casca);
print("%.2f" % alho);
print("%.2f" % oleo);