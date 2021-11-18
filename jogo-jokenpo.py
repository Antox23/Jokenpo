from time import sleep
from random import randint

itens = ["Pedra", "Papel", "Tesoura"]
computador = randint(0, 2)
nome = str(input("Insira seu nome:"))
print("Escolha sua jogada [0]Pedra [1] Papel [2] Tesoura")
jogador = int(input("Qual sua jogada, {}:".format(nome)))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")

print("Computador jogou, {}".format(itens[computador]))
print("{} jogou, {} ".format(nome, itens[jogador]))

print("-=" * 11)

if computador == 0:
    if jogador == 0:
        print("EMPATE!")

    elif jogador == 1:
        print({nome}, "ganhou!")

    elif jogador == 2:
        print("Computador ganhou")

    else:
        print("Ação inválida")

elif computador == 1:
    if jogador == 1:
        print("EMPATE!")

    elif jogador == 2:
        print({nome}, "ganhou!")

    elif jogador == 0:
        print("Computador perdeu")

    else:
        print("Ação inválida")

elif computador == 2:
    if jogador == 2:
        print("EMPATE!")
        
    elif jogador == 0:
        print({nome}, "ganhou!")

    elif jogador == 1:
        print("Computador perdeu")

    else:
        print("Ação inválida")