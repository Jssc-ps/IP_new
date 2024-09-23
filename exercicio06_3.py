from time import sleep

def tabuada (numero):
    for m in range (1, 11, 1):
        print(f'{nunero} X {m} = {numero*m}')
        sleep(1)
if __name__ == '__main__':
    número = int(input('Digite um número: '))
    tabuada(numero)