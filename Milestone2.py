#Jodo de cartas Milestone project 2 do curso de PAITOM!

#Criando a Classe Card que precisará de um naipe, a carta e o valor
# Os valores das cartas foram listados como variáveis globais
import random

naipes = ('Ouro', 'Espadas', 'Copas', 'Paus')
cartas = ('As', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Dama', 'Rei')
values = {'As': 1, 'Dois': 2, 'Tres': 3, 'Quatro': 4, 'Cinco': 5, 'Seis': 6, 'Sete': 7, 'Oito': 8,
          'Nove': 9, 'Dez': 10, 'Valete': 11, 'Dama': 12, 'Rei': 13}


class Card:
    def __init__(self, naipe, carta):
        self.naipe = naipe
        self.carta = carta
        self.value = values[carta]

    def __str__(self):
        return self.carta + " de " + self.naipe


# Criando uma classe para o Baralho

class Baralho:
    def __init__(self):

        self.todas_cartas = []

        for naipe in naipes:
            for carta in cartas:
                # Criando o objeto Carta
                criar_carta = Card(naipe, carta)

                self.todas_cartas.append(criar_carta)

    def embaralha(self):

        random.shuffle(self.todas_cartas)

    def add_uma(self):
        return self.todas_cartas.pop()


# Criando a classe de Jogador
class Jogador:

    def __init__(self, name):
        self.name = name
        self.todas_cartas = []

    def remove_uma(self):
        return self.todas_cartas.pop(0)

    def compra_uma(self, carta_nova):
        if type(carta_nova) == type([]):
            self.todas_cartas.extend(carta_nova)
        else:
            self.todas_cartas.append(carta_nova)

    def __str__(self):
        return f'O jogador {self.name} tem {len(self.todas_cartas)} cartas.'

#Setup do jogo

Jogador_1 = Jogador("Pelé")
Jogador_2 = Jogador("Maradona")

baralho_novo = Baralho()
baralho_novo.embaralha()

for x in range(26):
    Jogador_1.compra_uma(baralho_novo.add_uma())
    Jogador_2.compra_uma(baralho_novo.add_uma())

game_on = True
# Duração do game vai ser enquanto estiver "ON" kkkkk
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num} ")

    if len(Jogador_1.todas_cartas) == 0:
        print(f"{Jogador_1} está sem cartas. {Jogador_2} venceu!")
        game_on = False
        break

    if len(Jogador_2.todas_cartas) == 0:
        print(f"{Jogador_2} está sem cartas. {Jogador_1} venceu!")
        game_on = False
        break

# Começando um novo round

    Cartas_Jogador_1 = []
    Cartas_Jogador_1.append(Jogador_1.remove_uma())

    Cartas_Jogador_2 = []
    Cartas_Jogador_2.append(Jogador_2.remove_uma())

# Criando um padrão de jogo

    guerra = True

    while guerra:

        if Cartas_Jogador_1[-1].value > Cartas_Jogador_2[-1].value:
            Jogador_1.compra_uma(Cartas_Jogador_1)
            Jogador_1.compra_uma(Cartas_Jogador_2)

            guerra = False
        if Cartas_Jogador_1[-1].value < Cartas_Jogador_2[-1].value:
            Jogador_2.compra_uma(Cartas_Jogador_1)
            Jogador_2.compra_uma(Cartas_Jogador_2)

            guerra = False

        else:
            print("GUERRAAA!!!")

            if len(Jogador_1.todas_cartas) < 3:
                print(f"{Jogador_1} Não pode declarar guerra")
                print(f"{Jogador_2} Vence!")
                game_on = False
                break

            elif len(Jogador_2.todas_cartas) < 3:
                print(f"{Jogador_2} Não pode declarar guerra")
                print(f"{Jogador_1} Vence!")
                game_on = False
                break
            else:
                for num in range(3):
                    Cartas_Jogador_1.append(Jogador_1.remove_uma())
                    Cartas_Jogador_2.append(Jogador_2.remove_uma())
