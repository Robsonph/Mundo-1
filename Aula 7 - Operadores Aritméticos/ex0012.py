#Faça um algoritmo que leia o preço do produto e mostre seu novo preço, com 5% de desconto

#print('===========Consultor de Preço============')

p = float(input('Digite o preço do produto, R$: '))
por = p * 5 / 100
novo = p - por
print('Seu novo valor com deconto de 5% é R$:{}'.format(novo))

