distancia_dragao1 = float(input('Distância percorrida pelo Dragão 1 (km): '))
tempo_dragao1 = float(input('tempo do Dragão 1 (hora): '))

distancia_dragao2 = float(input('Distância percorrida pelo Dragão 2 (km): '))
tempo_dragao2 = float(input('tempo do Dragão 2 (hora): '))

velocidade_dragao1 = distancia_dragao1 / tempo_dragao1
velocidade_dragao2 = distancia_dragao2 / tempo_dragao2

if velocidade_dragao1 > velocidade_dragao2:
    print('dragão 1 é mais rápido!')
elif velocidade_dragao2 > velocidade_dragao1:
    print('dragão 2 é mais rápido')
else:
    print('ambos os dragões tem a mesma velocidade')