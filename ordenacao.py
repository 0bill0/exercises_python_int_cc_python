nu1 = int(input('Entre com o primeiro numero: '))
nu2 = int(input('Entre com o segundo numero: '))
nu3 = int(input('Entre com o terceiro numero: '))
if(nu1 < nu2 and nu1 < nu3 and nu2 < nu3):
    print('crescente')
else:
    print('não está em ordem crescente')
