import subprocess
import pygame
import sys
import random
from tkinter import messagebox

# inicializar o jogo
pygame.init()
pygame.mixer.init()

# configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Pong')

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Configurações da bola
bola_pos = [largura // 2, altura // 2]
bola_vel = [4, 4]
bola_raio = 15

# Configurações das raquetes
raquete_largura = 10
raquete_altura = 100
raquete1_pos = [50, altura // 2 - raquete_altura // 2]
raquete2_pos = [largura - 50 - raquete_largura, altura // 2 - raquete_altura // 2]
raquete_vel = 5

# Pontuação
placar1 = 0
placar2 = 0

# Velocidade máxima da bola
velocidade_maxima = 10

# sons
som_colisao = pygame.mixer.Sound("tablehit.mp3")
som_pontuacao = pygame.mixer.Sound("score.mp3")

# Função para desenhar elementos na tela
def desenhar():
    tela.fill(preto)

    # Desenhar a bola
    pygame.draw.circle(tela, branco, bola_pos, bola_raio)

    # Desenhar as raquetes
    pygame.draw.rect(tela, branco, (raquete1_pos[0], raquete1_pos[1], raquete_largura, raquete_altura))
    pygame.draw.rect(tela, branco, (raquete2_pos[0], raquete2_pos[1], raquete_largura, raquete_altura))

    # Desenhar o placar
    fonte = pygame.font.Font(None, 40)
    texto_placar = fonte.render(f"{placar1}   {placar2}", True, branco)
    tela.blit(texto_placar, (largura // 2 - 20, 20))

    pygame.display.flip()

# Função para reiniciar a bola
def reniciar_a_bola():
    global bola_vel
    bola_pos[0] = largura // 2
    bola_pos[1] = altura // 2
    bola_vel = [random.choice([4, -4]), random.choice([4, -4])]

# Função para a tela inicial ou de vitória
def tela_inicial(nome):
    while True:
        tela.fill(preto)
        fonte = pygame.font.Font(None, 60)
        mensagem = fonte.render(f"{nome} venceu!", True, branco)
        tela.blit(mensagem, (largura // 2 - mensagem.get_width() // 2, altura // 2 - mensagem.get_height() // 2))
        
        fonte_pontuacao = pygame.font.Font(None, 40)
        texto_placar = fonte_pontuacao.render(f"Placar: {placar1} - {placar2}", True, branco)
        tela.blit(texto_placar, (largura // 2 - texto_placar.get_width() // 2, altura // 2 + 50))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return  # Retorna para reiniciar o jogo ou terminar
                elif evento.key == pygame.K_q:  # Pressione Q para sair
                    try:
                        subprocess.Popen(['python', 'main.py'])  # Reinicia o jogo chamando main.py
                        pygame.quit()  # Fecha o Pygame
                        quit()  # Sai do programa
                    except Exception as e:
                        messagebox.showerror("Erro", f"Não foi possível voltar: {e}")

# Loop principal do jogo 
rodando = True
clock = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Movimento das raquetes
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete1_pos[1] > 0:
        raquete1_pos[1] -= raquete_vel
    if teclas[pygame.K_s] and raquete1_pos[1] < altura - raquete_altura:
        raquete1_pos[1] += raquete_vel
    if teclas[pygame.K_UP] and raquete2_pos[1] > 0:
        raquete2_pos[1] -= raquete_vel
    if teclas[pygame.K_DOWN] and raquete2_pos[1] < altura - raquete_altura:
        raquete2_pos[1] += raquete_vel

    # Movimento da bola
    bola_pos[0] += bola_vel[0]
    bola_pos[1] += bola_vel[1]

    # Colisão com o topo e a parte inferior da tela
    if bola_pos[1] <= bola_raio or bola_pos[1] >= altura - bola_raio:
        bola_vel[1] = -bola_vel[1]

    # Colisão com as raquetes
    colisao_com_raquete = False
    if (raquete1_pos[0] < bola_pos[0] < raquete1_pos[0] + raquete_largura and
            raquete1_pos[1] < bola_pos[1] < raquete1_pos[1] + raquete_altura):
        offset = (bola_pos[1] - (raquete1_pos[1] + raquete_altura / 2)) / (raquete_altura / 2)
        bola_vel[0] = abs(bola_vel[0])  # Garante que a bola vá para a direita
        bola_vel[1] += offset * 2  # Altera a direção vertical
        colisao_com_raquete = True
    
    if (raquete2_pos[0] < bola_pos[0] < raquete2_pos[0] + raquete_largura and
            raquete2_pos[1] < bola_pos[1] < raquete2_pos[1] + raquete_altura):
        offset = (bola_pos[1] - (raquete2_pos[1] + raquete_altura / 2)) / (raquete_altura / 2)
        bola_vel[0] = -abs(bola_vel[0])  # Garante que a bola vá para a esquerda
        bola_vel[1] += offset * 2  # Altera a direção vertical
        colisao_com_raquete = True

    # Se houve colisão, toca o som e aumenta a velocidade da bola
    if colisao_com_raquete:
        som_colisao.play()
        bola_vel[0] *= 1.1  # Aumenta a velocidade em 10%
        bola_vel[1] *= 1.1
        bola_vel[0] = max(min(bola_vel[0], velocidade_maxima), -velocidade_maxima)
        bola_vel[1] = max(min(bola_vel[1], velocidade_maxima), -velocidade_maxima)        

    # Pontuação
    if bola_pos[0] <= 0:
        placar2 += 1
        som_pontuacao.play()
        if placar2 == 10:
            tela_inicial("Jogador 2")  # Chama a tela de vitória para o Jogador 2
            placar1 = 0  # Reinicia os pontos
            placar2 = 0
        else:
            reniciar_a_bola()
        
    if bola_pos[0] >= largura:
        placar1 += 1
        som_pontuacao.play()
        if placar1 == 10:
            tela_inicial("Jogador 1")  # Chama a tela de vitória para o Jogador 1
            placar1 = 0  # Reinicia os pontos
            placar2 = 0
        else:
            reniciar_a_bola()

    # Desenhar os elementos na tela
    desenhar()

    # Controle a taxa de quadros do jogo
    clock.tick(60)

pygame.quit()
sys.exit()
