km = float(input('Quantos km foram rodados? '))
dias = int(input('Quantos dias o carro foi usado? '))
total = km * 0.15 + dias * 60
print('Você tera que pagar R${}'.format(total))
