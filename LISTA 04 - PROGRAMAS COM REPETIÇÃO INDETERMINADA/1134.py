# Alcool 1
# Gasolina 2
# Diesel 3
# Fim 4
comub = [0, 0, 0]
while True:
    cont = int(input())
    if cont == 1:
        comub[0] = comub[0] + 1
    elif cont == 2:
        comub[1] = comub[1] + 1
    elif cont == 3:
        comub[2] = comub[2] + 1
    elif cont == 4:
        print('MUITO OBRIGADO')
        print(f'Alcool: {comub[0]}\nGasolina: {comub[1]}\nDiesel: {comub[2]}')
        break
