#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

k = float(input('Quantos Km utilizou: '))
d = float(input('Quantos dias utilizou: '))
v1 = d * 60
v2 = k * 0.15
print('O valor a pagar pelos dias alugados é R$:{:.2f}\n E o valor pela Kilometragem é R$:{:.2f}'.format(v1, v2))
total = v1 + v2
print('Soma total R$:{}!'.format(total))
