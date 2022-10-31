"""
..........Pontifícia Universidade Católica do Paraná..........
............Análise e Desenvolvimento de Sistemas.............
....................Eduardo Kayke Da Silva....................
"""

# Jogo Zombie Dice

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
    try:
        print()
        jogadores = int(input("Quantos jogadores? --> "))

        if jogadores < 2:
            print("Para jogar você deve ter pelo menos 2 jogadores.")
        else:
            print()
            print(f"Temos {jogadores} Zombies, Aaaargh!")
            print(f"Cérebrooos, Aaaargh!")
            print()
    except:
        if jogadores != int:
            print("Não é aceito letras, digite apenas números.")


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

    # Função que sorteia um dado do copo de dados.
    sorteio = random.choice(copo_de_dados)

    # Função para adicionar mais informações sobre a face.

    def nome_face(dado):
        if dado == 'C':
            return f'Você comeu um cérebro.'
        elif dado == 'P':
            return f'Sua vítima escapou.'
        else:
            return f'Você levou um tiro.'

    # Sorteio das faces e retorno
    if sorteio == 'verde':
        verde = random.choice(faces_dado_verde)
        return f'Dado verde. Face sorteada --> {verde} --> {nome_face(verde)}'
    elif sorteio == 'amarelo':
        amarelo = random.choice(faces_dado_amarelo)
        return f'Dado amarelo. Face sorteada --> {amarelo} --> {nome_face(amarelo)}'
    else:
        vermelho = random.choice(faces_dado_vermelho)
        return f'Dado vermelho. Face sorteada --> {vermelho} --> {nome_face(vermelho)}'


# Função de pergunta Sim ou Não para rolar os dados.
def sim_nao_rolar():
    try:
        sim_ou_nao = str(input("Deseja rolar o dado? Sim(s) ou Não(n) --> "))

        if sim_ou_nao != 's' and sim_ou_nao != 'S' and sim_ou_nao != 'n' and sim_ou_nao != 'N':
            print()
            print('........................ATENÇÂO........................')
            print('......Digite apenas (s) para Sim ou (n) para Não.......')
            print()
        return sim_ou_nao
    except:
        if jogadores != int:
            print()
            print('........................ATENÇÂO........................')
            print("Não é aceito números, digite apenas letras, (s) ou (n).")
            print()


# Função para adicionar valores nas variáveis
def adicionar_valor(valor):

    global tiros, passos, cerebros

    if 'tiro' in valor:
        tiros += 1
    elif 'escapou' in valor:
        passos += 1
    elif 'cérebro' in valor:
        cerebros += 1
    else:
        print('Erro ao adicionar a variável')


# Variáveis iniciais para os turnos do jogo.
jogador_atual = 0
dados_sorteados = []
tiros = 0
cerebros = 0
passos = 0
jogada = 1
turno = 1

# Iniciando o jogo
print()
print("................O JOGO COMEÇOU.................")
print()
print("Os Zombies estão correndo e atacando as pessoas")
print("..........Cérebroooooos, Aaaaaaaargh...........")
print()

while True:
    print()
    print(
        f'Iniciando o turno {turno} com -->   >>>  {lista_jogadores[jogador_atual]}  <<<')
    print()
    print('Role os dados, boa sorte...')

    while jogador_atual < len(lista_jogadores):
        print()

        escolha = sim_nao_rolar()

        if escolha == 's' or escolha == 'S':
            print()
            print()
            print(f'..........................JOGADA {jogada}..........................')

            # Sortear o primeiro dado e adicionar o valor a variável.
            rolar1 = sortear_dados()
            print(rolar1)
            adicionar_valor(rolar1)

            # Sortear o segundo dado e adicionar o valor a variável.
            rolar2 = sortear_dados()
            print(rolar2)
            adicionar_valor(rolar2)

            # Sortear o terceiro dado e adicionar o valor a variável.
            rolar3 = sortear_dados()
            print(rolar3)
            adicionar_valor(rolar3)

            # Placar
            print()
            print('---------------------------PLACAR---------------------------')
            print(
                f'-------------Passos: {passos}, Tiros: {tiros}, Cérebros: {cerebros}---------------')
            print('............................................................')
            print()
            print()

            # Adicionando valor a jogada.
            jogada += 1

        else:

            print('............................................................')

            # Mudando o jogador
            jogador_atual += 1
            
            # Resetando as variáveis
            tiros = 0
            cerebros = 0
            passos = 0
            jogada = 1

            # Adicionando valor ao turno
            turno += 1

            # Parando o while
            break
    
    print()
    print('..................FIM DE JOGO..................')
    #if #jogador levou 3 tiros perdeu:
            
            #Apresentar jogador perdeu
    #elif #jogador comeu 13 cérebros ganhou:
        
        #Apresentar jogador perdeu

# . Se o jogador comeu 13 cérebros.
#     Mostrar o nome do jogador
#     Mensagem de vitória
# . Fim do jogo
# . Opções para jogar novamente ou sair.


# Modificou a estrutura dos dados de string para tupla​
# Utilizou uma estrutura para armazenar os jogadores​
# Utilizou uma estrutura para armazenar os dados do jogo (simular o copo)​
# Remove os dados da lista em cada jogada​
# Armazena a pontuação dos jogadores na lista (quantidade de cérebros e tiros)​
# Reinicia a lista que armazena os dados sempre que o turno de um jogador termina (adicionado novamente os 13 dados no copo)​
# Reinicia a pontuação de tiros na lista sempre que o jogador finalizar seu turno​
# Imprime na saída do console quais os dados que estão armazenados no copo em cada uma das jogadas ​