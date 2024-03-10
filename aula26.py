'''
Formatação básica de strings
s - string
d - int
f - float
.< números de dígitos>f
x ou X - Hexadecimal
(caractere)(<>^)(quantidade)
> - Esquerda
< - Direita
^ - centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: >10}')
print(f'{variavel: ^10}')
print(f'{12.12837187631: ,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')