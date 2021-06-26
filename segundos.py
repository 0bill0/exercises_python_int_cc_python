'''Este é o desafio do vídeo "Entrada de Dados".

Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:
2 dias, 1 horas, 36 minutos e 55 segundos.'''
segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

b = total_segs // 3600
d = total_segs % 3600
c = d // 60
d = d % 60
a = b // 24
b = b % 24

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")