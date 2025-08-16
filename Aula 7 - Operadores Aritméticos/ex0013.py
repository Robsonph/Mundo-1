#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

s = float(input('Digite o salario do funcionario, R$:'))
por = s + (s * 15 / 100)
print('O novo salario do funcionario com 15% de aumento é R$:{}'.format(por))