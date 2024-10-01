import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, Text, Scrollbar, END, BOTH, RIGHT, Y

# Função para selecionar o ficheiro de texto
def selecionar_txt():
    caminho_txt = filedialog.askopenfilename(filetypes=[("Ficheiros de Texto", "*.txt")])
    entry_txt.delete(0, 'end')  # Limpa o campo de entrada
    entry_txt.insert(0, caminho_txt)  # Insere o caminho do ficheiro selecionado
    atualizar_previsualizacao()  # Atualiza a pré-visualização

# Função para selecionar uma imagem
def selecionar_imagem():
    caminho_imagem = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpeg")])
    entry_imagem.delete(0, 'end')
    entry_imagem.insert(0, caminho_imagem)
    atualizar_previsualizacao()

# Função para selecionar um vídeo
def selecionar_video():
    caminho_video = filedialog.askopenfilename(filetypes=[("Vídeos", "*.mp4")])
    entry_video.delete(0, 'end')
    entry_video.insert(0, caminho_video)
    atualizar_previsualizacao()

# Função para atualizar a pré-visualização do conteúdo em Markdown
def atualizar_previsualizacao():
    conteudo_md = converter_para_markdown()
    campo_previsualizacao.delete(1.0, END)  # Limpa o campo de pré-visualização
    campo_previsualizacao.insert(END, conteudo_md)  # Insere o conteúdo convertido em Markdown

# Função para gravar o ficheiro em Markdown
def gravar_markdown():
    caminho_md = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown", "*.md")])
    if caminho_md:
        with open(caminho_md, 'w', encoding='utf-8') as f_md:  # Grava em UTF-8
            f_md.write(converter_para_markdown())  # Grava o conteúdo convertido para Markdown
        messagebox.showinfo("Sucesso", "Ficheiro Markdown gravado com sucesso!")

# Função para converter o ficheiro .txt para Markdown
def converter_para_markdown():
    caminho_txt = entry_txt.get()  # Obtém o caminho do ficheiro .txt
    caminho_imagem = entry_imagem.get()  # Obtém o caminho da imagem
    caminho_video = entry_video.get()  # Obtém o caminho do vídeo

    # Verifica se o ficheiro de texto existe
    if not os.path.exists(caminho_txt):
        return "Erro: O ficheiro de texto não foi encontrado."

    # Tenta ler o ficheiro .txt em UTF-8
    try:
        with open(caminho_txt, 'r', encoding='utf-8') as f_txt:
            conteudo_txt = f_txt.read()
    except UnicodeDecodeError:
        return "Erro: Não foi possível decodificar o ficheiro de texto. Verifique a codificação."

    # Formata o conteúdo em Markdown
    conteudo_md = f"# Conteúdo do Ficheiro\n\n{conteudo_txt}\n\n"

    # Se uma imagem foi selecionada, adiciona ao Markdown
    if caminho_imagem and os.path.exists(caminho_imagem):
        nome_imagem = os.path.basename(caminho_imagem)  # Obtém o nome da imagem
        conteudo_md += f"![Imagem]({nome_imagem})\n\n"

    # Se um vídeo foi selecionado, adiciona o link para o vídeo
    if caminho_video and os.path.exists(caminho_video):
        nome_video = os.path.basename(caminho_video)  # Obtém o nome do vídeo
        conteudo_md += f"[Ver Vídeo]({nome_video})\n\n"

    return conteudo_md  # Retorna o conteúdo em formato Markdown

# Criação da janela principal da aplicação
janela = Tk()
janela.title("Conversor de .txt para Markdown com Pré-visualização")

# Campo para o ficheiro de texto
Label(janela, text="Ficheiro .txt:").grid(row=0, column=0, padx=10, pady=10)
entry_txt = Entry(janela, width=50)
entry_txt.grid(row=0, column=1, padx=10, pady=10)
Button(janela, text="Selecionar", command=selecionar_txt).grid(row=0, column=2, padx=10, pady=10)

# Campo para o ficheiro de imagem
Label(janela, text="Imagem (.jpeg):").grid(row=1, column=0, padx=10, pady=10)
entry_imagem = Entry(janela, width=50)
entry_imagem.grid(row=1, column=1, padx=10, pady=10)
Button(janela, text="Selecionar", command=selecionar_imagem).grid(row=1, column=2, padx=10, pady=10)

# Campo para o ficheiro de vídeo
Label(janela, text="Vídeo (.mp4):").grid(row=2, column=0, padx=10, pady=10)
entry_video = Entry(janela, width=50)
entry_video.grid(row=2, column=1, padx=10, pady=10)
Button(janela, text="Selecionar", command=selecionar_video).grid(row=2, column=2, padx=10, pady=10)

# Botão para converter e gravar o ficheiro em Markdown
Button(janela, text="Converter e Gravar", command=gravar_markdown).grid(row=3, column=1, padx=10, pady=20)

# Campo de pré-visualização do conteúdo Markdown
Label(janela, text="Pré-visualização do Markdown:").grid(row=4, column=0, columnspan=3, padx=10, pady=10)
campo_previsualizacao = Text(janela, height=15, width=80)
campo_previsualizacao.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Scrollbar para o campo de pré-visualização
scrollbar = Scrollbar(janela)
scrollbar.grid(row=5, column=3, sticky='nsew')
campo_previsualizacao.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=campo_previsualizacao.yview)

# Iniciar a interface gráfica
janela.mainloop()
