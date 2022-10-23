import random

def sortear_dados():
    faces_dado_verde = ['C', 'P', 'C', 'T', 'P', 'C']
    faces_dado_amarelo = ['T', 'P', 'C', 'T', 'P', 'C']
    faces_dado_vermelho = ['T', 'P', 'T', 'C', 'P', 'T']

    copo_de_dados = ['verde', 'verde', 'verde', 'verde', 'verde', 'verde', 'amarelo',
                     'amarelo', 'amarelo', 'amarelo', 'vermelho', 'vermelho', 'vermelho']

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

print(sortear_dados())