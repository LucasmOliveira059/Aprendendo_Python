from random import randint
from time import  sleep

itens = ('Pedra', 'Papel', 'Tesoura')
cores = {
    'amarelo': '\033[33m',
    'vermelho': '\033[31m',
    'resultado': '\033[41m',
    'padrao': '\033[m'}
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual é sua jogada? '))
print('{}JO{}'.format(cores['resultado'], cores['padrao']))
sleep(1)
print('{}KEN{}'.format(cores['vermelho'], cores['padrao']))
sleep(1)
print('{}PO!!!{}'.format(cores['resultado'], cores['padrao']))
print('-=' *11)
print('{}Computador{} Jogou {}'.format(cores['vermelho'], cores['padrao'], itens[computador]))
print('{}Jogador{}    Jogou {}'.format(cores['amarelo'], cores['padrao'], itens[jogador]))
print('-=' *11)

if computador == 0:
    if jogador == 0:
        print('{}EMPATE{}'.format(cores['resultado'], cores['padrao']))
    elif jogador == 1:
        print('O {}Jogador{} {}GANHOU{}'.format(cores['amarelo'], cores['padrao'], cores['resultado'], cores['padrao']))
    elif jogador == 2:
        print('O {} Computador{} {}Venceu!{}'.format(cores['vermelho'], cores['padrao'], cores['resultado'], cores['padrao']))
elif computador == 1:
    if jogador == 1:
        print('{}EMPATE{}'.format(cores['resultado'], cores['padrao']))
    elif jogador == 2:
        print('O {}Jogador{} {}GANHOU{}'.format(cores['amarelo'], cores['padrao'], cores['resultado'], cores['padrao']))
    elif jogador == 0:
        print('O {} Computador{} {}Venceu!{}'.format(cores['vermelho'], cores['padrao'], cores['resultado'], cores['padrao']))
elif computador == 2:
    if jogador == 2:
        print('{}EMPATE{}'.format(cores['resultado'], cores['padrao']))
    elif jogador == 0:
        print('O {}Jogador{} {}GANHOU{}'.format(cores['amarelo'], cores['padrao'], cores['resultado'], cores['padrao']))
    elif jogador == 1:
        print('O {} Computador{} {}Venceu!{}'.format(cores['vermelho'], cores['padrao'], cores['resultado'], cores['padrao']))