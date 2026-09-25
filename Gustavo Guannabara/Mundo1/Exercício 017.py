from math import pow,sqrt
catOposto = float(input('Digite o cateto oposto:'))
catAdjacente = float(input('Digite o cateto adjacente:'))
hipotenusa = sqrt(pow(catOposto, 2)+pow(catAdjacente,2) )
print('Se o cateto oposto é {} e o cateto adjacente é {}  a hipotenunsa será igual a {}' .format(catOposto,catAdjacente,hipotenusa))