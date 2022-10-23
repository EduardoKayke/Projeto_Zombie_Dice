"""
Criou as variáveis para contabilizar os tiros, cérebros e passos​
Incrementa as variáveis quando um dos dados é lançado​
Implementou a rotina para sortear os dados dentro da estrutura de repetição​
Implementou a rotina para jogar os dados dentro da estrutura de repetição​
Criou as variáveis para contabilizar os tiros, cérebros e passos adicionando na estrutura de repetição​
Incrementa as variáveis quando um dos dados são lançados​
Verifica o resultado dos três dados lançados​
"""
# Importando o random.
import random

# Variáveis iniciais.
jogadores = 0
lista_jogadores = []

# Apresentação do jogo.
print("----------------------------------------")
print("--------Bem-Vindo ao Zombie Dice--------")
print("----------------Aaaargh!----------------")
print("----------------------------------------")
print("-----Para vencer coma 13 cérebrooos!----")
print("----------------------------------------")

# Entrada de dado da quantidade de jogadores.
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

# Entrada de dado do nome dos jogadores.
print(f"Qual é o nome dos Zombies?")

for index in range(jogadores):
    nome = input(f"Zombie {str(index + 1)}, qual é o seu nome? --> ")

    lista_jogadores.append(nome)


# Função que sorteia os dados.
def sortear_dados():
    # Faces dos dados verde, amarelo e vermelho
    faces_dado_verde = ['C', 'P', 'C', 'T', 'P', 'C']
    faces_dado_amarelo = ['T', 'P', 'C', 'T', 'P', 'C']
    faces_dado_vermelho = ['T', 'P', 'T', 'C', 'P', 'T']

    # Copo com os 13 dados para sorteio
    copo_de_dados = ['verde', 'verde', 'verde', 'verde', 'verde', 'verde', 'amarelo',
                     'amarelo', 'amarelo', 'amarelo', 'vermelho', 'vermelho', 'vermelho']

    #Função que sorteia um dado do copo de dados.
    sorteio = random.choice(copo_de_dados)

    # Função para adicionar mais informações sobre a face.
    def nome_face(dado):
        if dado == 'C':
            return f'Cérebros'
        elif dado == 'P':
            return f'Passos'
        else: 
            return f'Tiros'

    # Sorteio das faces e retorno
    if sorteio == 'verde':
        verde = random.choice(faces_dado_verde)
        return f'Dado verde. Face sorteada --> {verde} de {nome_face(verde)}'
    elif sorteio == 'amarelo':
        amarelo = random.choice(faces_dado_amarelo)
        return f'Dado amarelo. Face sorteada --> {amarelo} de {nome_face(amarelo)}'
    else:
        vermelho = random.choice(faces_dado_vermelho)
        return f'Dado vermelho. Face sorteada --> {vermelho} de {nome_face(vermelho)}'

# Variáveis iniciais para os turnos do jogo.
jogador_atual = 0
dados_sorteados = []
tiros = 0
cerebros = 0
passos = 0

# Iniciando o jogo
print("Jogando...")

while True:
    break
# A ideia é.. Cada jogador em seu turno sorteia os dados para jogar..
# Vc não deve sortear para todos os jogadores
# Cada um na sua vez pega o copo com 3 dados..
# E sorteia 3 dados para jogar..
# E desses 3 dados sorteia uma das 6 faces de cada dado

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
