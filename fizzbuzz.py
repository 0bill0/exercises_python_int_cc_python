num = int(input('Insira o numero e saiba se ele eh divisível por 3 e 5 Simultaneamente: '))
if(num%5==0 and num%3==0):
    print('FizzBuzz')
else:
    print(num)