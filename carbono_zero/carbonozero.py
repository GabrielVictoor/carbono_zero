import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def calcular_impacto():
    combustivel = float(entrada_combustivel.get())
    eletricidade = float(entrada_eletricidade.get())
    transporte = float(entrada_transporte.get())
    total_tCO2e = combustivel + eletricidade + transporte
    preco_credito = float(entrada_preco_credito.get())
    total_kg = total_tCO2e * 1000
    arvores_necessarias = total_kg / 22 
    compensacao = total_tCO2e * preco_credito
    resultado.config(text=f"Compensação: R${compensacao:.2f}\nÁrvores necessárias: {arvores_necessarias:.2f} árvores")

janela = tk.Tk()
janela.title("Calculadora de Emissões de Carbono")

descricao_inicial = tk.Label(janela, text="Insira abaixo a quantidade de dióxido de carbono (em tCO2e) emitidos nos seguintes escopos:")
descricao_inicial.grid(row=0, column=0, columnspan=2, pady=5)

descricao_atencao = tk.Label(janela, text="ATENÇÃO: Utilize '.' ao invés de ',' para separar as casas decimais.")
descricao_atencao.grid(row=1, column=0, columnspan=2, pady=5)

lbl_combustivel = tk.Label(janela, text="Combustível (tCO2e):")
lbl_combustivel.grid(row=2, column=0, sticky=tk.W+tk.E, padx=10, pady=5)
entrada_combustivel = tk.Entry(janela)
entrada_combustivel.grid(row=3, column=0, sticky=tk.W+tk.E, padx=10, pady=5)

lbl_eletricidade = tk.Label(janela, text="Eletricidade (tCO2e):")
lbl_eletricidade.grid(row=4, column=0, sticky=tk.W+tk.E, padx=10, pady=5)
entrada_eletricidade = tk.Entry(janela)
entrada_eletricidade.grid(row=5, column=0, sticky=tk.W+tk.E, padx=10, pady=5)

lbl_transporte = tk.Label(janela, text="Transporte (tCO2e):")
lbl_transporte.grid(row=6, column=0, sticky=tk.W+tk.E, padx=10, pady=5)
entrada_transporte = tk.Entry(janela)
entrada_transporte.grid(row=7, column=0, sticky=tk.W+tk.E, padx=10, pady=5)

lbl_preco_credito = tk.Label(janela, text="Preço do Crédito de Carbono (R$/tCO2e):")
lbl_preco_credito.grid(row=8, column=0, sticky=tk.W+tk.E, padx=10, pady=5)
entrada_preco_credito = tk.Entry(janela)
entrada_preco_credito.grid(row=9, column=0, sticky=tk.W+tk.E, padx=10, pady=5)

calcular_button = tk.Button(janela, text="Calcular", command=calcular_impacto)
calcular_button.grid(row=10, column=0, pady=10)

resultado = tk.Label(janela, text="")
resultado.grid(row=11, column=0, pady=10)

img_arvore = Image.open("tree.png")
img_arvore = img_arvore.resize((32, 32))
img_arvore = ImageTk.PhotoImage(img_arvore)
img_label = tk.Label(janela, image=img_arvore)
img_label.grid(row=12, column=0, pady=10)

for i in range(13): 
    janela.grid_rowconfigure(i, weight=1)
janela.grid_columnconfigure(0, weight=1)

janela.mainloop()
