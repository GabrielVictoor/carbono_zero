import tkinter as tk
from tkinter import PhotoImage  # Importar a classe PhotoImage do tkinter
from PIL import Image, ImageTk  # Importar o módulo Image e a classe ImageTk do Pillow

# Função para calcular o impacto e o plantio de árvores necessárias
def calcular_impacto():
    tCO2e = float(entrada_tCO2e.get())
    preco_credito = float(entrada_preco_credito.get())
    compensacao = tCO2e * preco_credito
    arvores_necessarias = tCO2e / 7  # 7 árvores por tonelada
    resultado.config(text=f"Compensação: R${compensacao:.2f}\nÁrvores necessárias: {arvores_necessarias:.2f} (em até 20 anos)")
    
# interface
janela = tk.Tk()
janela.title("Calculadora de Emissões de Carbono")

# inputs
lbl_tCO2e = tk.Label(janela, text="Emissões de Carbono (tCO2e):")
# Usando o método grid para posicionar o widget
# O parâmetro sticky é usado para fazer o widget se expandir na direção horizontal
lbl_tCO2e.grid(row=0, column=0, sticky=tk.W+tk.E, padx=10, pady=5)
entrada_tCO2e = tk.Entry(janela)
entrada_tCO2e.grid(row=1, column=0, sticky=tk.W+tk.E, padx=10, pady=5)

lbl_preco_credito = tk.Label(janela, text="Preço do Crédito de Carbono (R$/tCO2e):")
lbl_preco_credito.grid(row=2, column=0, sticky=tk.W+tk.E, padx=10, pady=5)
entrada_preco_credito = tk.Entry(janela)
entrada_preco_credito.grid(row=3, column=0, sticky=tk.W+tk.E, padx=10, pady=5)

# Button
calcular_button = tk.Button(janela, text="Calcular", command=calcular_impacto)
calcular_button.grid(row=4, column=0, pady=10)

# resultado
resultado = tk.Label(janela, text="")
resultado.grid(row=5, column=0, pady=10)

# Carregar a imagem da árvore
img_arvore = Image.open("tree.png")
img_arvore = img_arvore.resize((32, 32))
img_arvore = ImageTk.PhotoImage(img_arvore)
img_label = tk.Label(janela, image=img_arvore)
img_label.grid(row=6, column=0, pady=10)

# Configurando o redimensionamento
for i in range(7):  # Porque temos 7 rows
    # grid_rowconfigure com weight=1 faz com que a linha expanda proporcionalmente quando a janela é redimensionada
    janela.grid_rowconfigure(i, weight=1)
# grid_columnconfigure com weight=1 faz com que a coluna expanda proporcionalmente quando a janela é redimensionada
janela.grid_columnconfigure(0, weight=1)

janela.mainloop()
