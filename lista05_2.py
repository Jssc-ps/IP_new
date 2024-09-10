ferro = float(input('digite a quantidade de ferro em kg: '))
ouro = float(input('digite a quantidade de ouro em kg: '))

total = ferro + ouro
porcentagem_ferro = (ferro / ferro + ouro) * 100

if porcentagem_ferro >= 70:
    print('A liga metálica está adequada!')
else:
    print('A liga metálica não é adequada, precisa de mais ferro.')