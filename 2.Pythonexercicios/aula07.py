nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))


n1 = int(input('Digite um numero? '))
n2 = int(input('Digite outro numero? '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print(' A soma vale {}. \n o produto é {}. \n e a divisão é {:.1f}\n'.format(s, m, d), end=' ')
print('Divisão inteira {}. \n e potência {}.\n O resto da divisão é {}\n'.format(di, e, r), end=' ')

print('========Quer ver algo interessamte?==========')
ver = input('Digite fuck no teclado!! ')
print('VC É FODA')