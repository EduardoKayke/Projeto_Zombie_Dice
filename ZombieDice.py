"""
Utilizou as estruturas condicionais (if, else e elif)​
Utilizou os operadores lógicos e aritméticos ​
Criou os  dados utilizando uma string (6 verdes, 4 amarelos e 3 vermelhos) ​
Implementou a rotina para sortear os dados (selecionar três dados)
Implementou a rotina para jogar os dados (sortear a face de um dos dados)
Criou as variáveis para contabilizar os tiros, cérebros e passos​
Incrementa as variáveis quando um dos dados é lançado​
Utilizou as estruturas repetição (for e while)
Realiza a Interação do jogador utilizando a estrutura de repetição​
Implementou a rotina para sortear os dados dentro da estrutura de repetição​
Implementou a rotina para jogar os dados dentro da estrutura de repetição​
Criou as variáveis para contabilizar os tiros, cérebros e passos adicionando na estrutura de repetição​
Incrementa as variáveis quando um dos dados são lançados​
Verifica o resultado dos três dados lançados​


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

for nome_jogadores in len(jogadores):
    nome_jogadores = input(f"Zombie {nome_jogadores}. Qual seu nome?")
    

# . Usuário deve informar o nome dos jogadores
#     Mostrar o nome dos jogadores

# Assim, você deverá criar os dados neste momento utilizando um objeto do tipo string. 
# Esta string deve conter seis caracteres para simular cada face do dado. Para 
# identificar as faces dos dados segue abaixo especificação:
# 6 Dados verdes: “CPCTPC”
# 4 Dados amarelos: “TPCTPC”
# 3 Dados vermelhos: “TPTCPT”
# Onde, o caractere “C” na string corresponde ao cérebro, caractere “P” são os passos e 
# por fim o “T” é o tiro.
# Neste momento você deve utilizar a string de forma aleatória, poderá utilizar a função 
# random.choice() ou se preferir poderá trabalhar com o índice da string.
# Assim, utilizando os dados, você já consegue começar a trabalhar com a lógica do jogo. 
# Consegue definir blocos de código utilizando as estruturas condicionais, ou seja, 
# quando o jogador cair em cada um das faces do dado, poderá incrementar um contador 
# (cérebro, passos 

# . Se o jogador comeu 13 cérebros.
#     Mostrar o nome do jogador
#     Mensagem de vitória
# . Fim do jogo
# . Opções para jogar novamente ou sair.