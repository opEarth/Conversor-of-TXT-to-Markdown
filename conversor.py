import tkinter as tk
from tkinter import filedialog
import os
from moviepy.editor import VideoFileClip

def converter_txt_para_markdown():
    # Obter os caminhos dos arquivos
    caminho_txt = entrada_txt.get()
    caminho_saida = entrada_saida.get()
    caminho_imagens = entrada_imagens.get()
    caminho_video = entrada_video.get()

    # Ler o arquivo .txt
    with open(caminho_txt, 'r') as f:
        texto = f.read()

    # Substituir os marcadores de imagem e vídeo por sintaxes Markdown
    texto = texto.replace('[imagem]', f'![imagem]({os.path.join(caminho_imagens, "imagem.jpg")})')  # Ajustar o nome da imagem
    clip = VideoFileClip(os.path.join(caminho_video, "video.mp4"))  # Ajustar o nome do vídeo
    texto = texto.replace('[video]', f'[{clip.duration}s video]({clip.ipython_repr()})')

    # Salvar o arquivo Markdown
    with open(caminho_saida, 'w') as f:
        f.write(texto)

    # Mostrar mensagem de sucesso
    label_resultado['text'] = 'Conversão realizada com sucesso!'

# Criar a janela principal
janela = tk.Tk()
janela.title("Conversor TXT para Markdown")

# Criar os elementos da interface
label_txt = tk.Label(janela, text="Selecione o arquivo .txt:")
entrada_txt = tk.Entry(janela)
botao_procurar_txt = tk.Button(janela, text="Procurar", command=lambda: entrada_txt.insert(0, filedialog.askopenfilename()))

# ... (similar para os outros campos)

# Botão para converter
botao_converter = tk.Button(janela, text="Converter", command=converter_txt_para_markdown)

# Label para mostrar o resultado
label_resultado = tk.Label(janela, text="")

# ... (posicionar os elementos na janela)

janela.mainloop()