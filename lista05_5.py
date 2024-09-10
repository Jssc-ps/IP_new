agua_disponivel = float(input('quantidade de água disponível: '))

distancia = float(input('distância até o oásis (km):'))

agua_necessaria = distancia * 2

if agua_disponivel >= agua_necessaria:
    print('a quantidade de água é suficiente para chegar no oásis.')

else:
    print('a quantidade de água não é suficiente, será necessário mais água.')