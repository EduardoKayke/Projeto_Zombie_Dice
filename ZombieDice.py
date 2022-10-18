"""
Utilizou as estruturas condicionais (if, else e elif)​
Utilizou os operadores lógicos e aritméticos ​
Criou os  dados utilizando uma string (6 verdes, 4 amarelos e 3 vermelhos) ​
Adicionou a entrada para receber o jogadores​
Implementou a rotina para sortear os dados (selecionar três dados)
Implementou a rotina para jogar os dados (sortear a face de um dos dados)
Implementou a entrada para receber a quantidade de jogadores ​
Efetua checagem se foi adicionado pelo menos dois jogadores​
Criou as variáveis para contabilizar os tiros, cérebros e passos​
Incrementa as variáveis quando um dos dados é lançado​
"""
print("----------------------------------------")
print("--------Bem-Vindo ao Zombie Dice--------")
print("----------------Aaaargh!----------------")
print("----------------------------------------")
print("-----Para vencer coma 13 cérebrooos!----")
print("----------------------------------------")

jogadores = 0

while jogadores < 2:
    print()
    jogadores = int(input("Quantos jogadores? --> "))

    if jogadores < 2:
        print("Para jogar você deve ter pelo menos 2 jogadores.")
    else:
        print()
        print(f"Temos {jogadores} Zombies, Aaaargh!")
        print(f"Cérebrooos, Aaaargh!")
        print()

print("Qual é o nome dos Zombies?")

nome_jogadores = []

while nome_jogadores < len(jogadores):
    nome_jogadores = input(f"Zombie {nome_jogadores}. Qual seu nome?")
    
#     Mostrar o número de jogadores
# . Usuário deve informar o nome dos jogadores
#     Mostrar o nome dos jogadores

# . Se o jogador comeu 13 cérebros.
#     Mostrar o nome do jogador
#     Mensagem de vitória
# . Fim do jogo
# . Opções para jogar novamente ou sair.