def metros_para_milimetros():
    try:
        metros = float(input('Valor: '))
        milimetros = metros * 1000
        centimetros = metros / 100
        print(f"{metros} metros equivale a {milimetros:.2f} milimetros e {centimetros:.2f} centimetros.")
    except ValueError:
        print('por favor digite um numero valido.')

metros_para_milimetros()
