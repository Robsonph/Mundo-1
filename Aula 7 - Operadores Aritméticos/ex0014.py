#Escreva um programa que converta uma temperatura digitada em ºC
#e converta para ºF'''

c = float(input('Digite a temperatura em ºC: '))
f = (c * 9 / 5) + 32
print('A temperatura {}ºC em fahrenheit é {}ºF!'.format(c, f))
