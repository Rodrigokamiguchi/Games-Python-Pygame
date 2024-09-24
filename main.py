import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def iniciar_jogo():
    nome_jogador = entry_nome.get()
    if nome_jogador.strip() == "":
        messagebox.showwarning("Aviso", "Por favor, insira um nome válido.")
        return
    
    try:
        subprocess.Popen(['python', 'snaker.py', nome_jogador])
        tela_inicial.destroy()  # Fecha a tela inicial após iniciar o jogo
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível iniciar o jogo: {e}")

# Usando o caminho absoluto da imagem
caminho_imagem = r"C:\Users\rodrigo.kamiguchi\Desktop\snaker\cobrinha.jpg"  # Ajuste o caminho se necessário
if not os.path.exists(caminho_imagem):
    raise FileNotFoundError(f"O arquivo {caminho_imagem} não foi encontrado.")

# Criação da tela inicial
tela_inicial = tk.Tk()
tela_inicial.title("Tela Inicial do Jogo")
tela_inicial.geometry("400x300")  # Ajusta o tamanho da janela
tela_inicial.configure(bg="#2C3E50")  # Define uma cor de fundo

# Label e Entry para o nome do jogador
label_nome = tk.Label(tela_inicial, text="Insira seu nome:", bg="#2C3E50", fg="#ECF0F1", font=("Helvetica", 14))
label_nome.pack(pady=20)

entry_nome = tk.Entry(tela_inicial, font=("Helvetica", 14), width=20)
entry_nome.pack(pady=10)

# Carregar a imagem do botão
imagem_botao = Image.open(caminho_imagem)  # Certifique-se de que este caminho está correto
imagem_botao = imagem_botao.resize((100, 100), Image.LANCZOS)  # Redimensiona a imagem
imagem_botao_tk = ImageTk.PhotoImage(imagem_botao)

# Botão para iniciar o jogo
botao_iniciar = tk.Button(tela_inicial, image=imagem_botao_tk, command=iniciar_jogo,
                          bg="#27AE60", fg="#FFFFFF", font=("Helvetica", 14), padx=10, pady=5)
botao_iniciar.pack(pady=30)

# Iniciar o loop da interface gráfica
tela_inicial.mainloop()
