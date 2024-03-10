name = input('Digite seu nome')
years = input('Digite sua idade')
if name and years:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')
    if ' ' in name:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')
    print(f'Seu nome tem {len(name)} letras')
    print(f'A primeira letra do seu nome é {name[0]}')
    print(f'A última letra do seu nome é {name[-1]}')
else:
    print('Desculpa, você deixou campos vazios')