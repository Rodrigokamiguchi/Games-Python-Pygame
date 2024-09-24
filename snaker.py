import tkinter as tk
from tkinter import messagebox
import pygame
import time
import random
import sqlite3
import sys
import subprocess

# Função principal que inicia o jogo
def main(nome_jogador):
    print(f"Iniciando o jogo da cobrinha para: {nome_jogador}")
    tela_inicial(nome_jogador)

# Conexão com o banco de dados
conn = sqlite3.connect('highscores.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)')
conn.commit()

# Cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Dimensões da tela
width = 600
height = 400

# Inicialização do Pygame
pygame.init()

# Criação da tela do jogo
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogo da Cobrinha')

# Controle da cobrinha
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Carregar imagens
snake_image = pygame.image.load('snake.jpg')  # Imagem da cobra
food_image = pygame.image.load('ratinho.png')  # Imagem da comida
background_image = pygame.image.load('grama.jpg')  # Imagem de fundo


# Fonte para a pontuação
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

def nossa_cobrinha(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def nosso_pontuacao(score):
    value = score_font.render("Pontuação: " + str(score), True, black)
    screen.blit(value, [0, 0])

def mensagem(msg, color, y_offset=0):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3 + y_offset])

def exibir_record():
    c.execute('SELECT name, score FROM scores ORDER BY score DESC LIMIT 10')
    return c.fetchall()

def tela_inicial(nome_jogador):
    screen.fill(blue)
    mensagem("Bem-vindo ao Jogo da Cobrinha!", white)
    mensagem("Pressione Enter para jogar", white, 30)

    # Mostra as 10 melhores pontuações
    records = exibir_record()
    y_offset = height / 2 + 20
    mensagem("Melhores Pontuações:", white, 60)

    for i, record in enumerate(records):
        mensagem(f"{i + 1}. {record[0]}: {record[1]} pontos", white, 90 + i * 30)

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                    gameLoop(nome_jogador)  # Inicia o jogo passando o nome do jogador
                elif event.key == pygame.K_q:  # Pressione Q para sair
                    try:
                        subprocess.Popen(['python', 'main.py'])
                        pygame.quit()  # Fecha o Pygame
                        quit()  # Sai do programa
                    except Exception as e:
                        messagebox.showerror("Erro", f"Não foi possível voltar: {e}")

def mostrar_pontuacao_alta(nome):
    c.execute('SELECT MAX(score) FROM scores WHERE name = ?', (nome,))
    max_score = c.fetchone()[0]
    screen.fill(blue)
    mensagem(f"Pontuação mais alta: {max_score}", white, 0)
    pygame.display.update()
    time.sleep(3)  # Espera 3 segundos para o jogador ver a pontuação
    tela_inicial(nome)  # Retorna à tela inicial

def gameLoop(nome):  # criando uma função do jogo
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            screen.fill(blue)
            mensagem("Você perdeu! Pressione C para continuar ou "
                     "Q para sair.", red)
            nosso_pontuacao(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        mostrar_pontuacao_alta(nome)  # Exibe a pontuação mais alta antes de sair
                        game_over = True
                    if event.key == pygame.K_c:
                        # Adiciona a pontuação ao banco de dados
                        c.execute('INSERT INTO scores (name, score) VALUES (?, ?)', (nome, Length_of_snake - 1))
                        conn.commit()
                        tela_inicial(nome)  # Volta para a tela inicial
                        return  # Retorna para permitir novo jogo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True  # Aqui, vamos permitir que o jogo feche e volte à tela inicial
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_ESCAPE:  # Pressione ESC para voltar à tela inicial
                    tela_inicial(nome)  # Retorna à tela inicial
                    return  # Retorna para permitir novo jogo

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        nossa_cobrinha(snake_block, snake_List)
        nosso_pontuacao(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Inicia o jogo
if __name__ == "__main__":
    if len(sys.argv) > 1:
        jogador_nome = sys.argv[1]
        main(jogador_nome)
    else:
        jogador_nome = "Jogador"  # Nome padrão se não for fornecido
        main(jogador_nome)

# Fecha a conexão com o banco de dados ao sair
conn.close()
