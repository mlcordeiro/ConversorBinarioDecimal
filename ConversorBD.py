import tkinter as tk
from tkinter import messagebox

# Janela Principal
janela = tk.Tk()
janela.title('Conversor Binário-Decimal')
janela.geometry('450x500')
janela.configure(bg="#6C63FF")  # Um roxo mais moderno

# Título
titulo = tk.Label(
    janela,
    text='Conversor Binário - Decimal',
    font=('Verdana', 18, 'bold'),
    bg='#6C63FF',
    fg='white'
)
titulo.pack(padx=20, pady=30)

# Funções
def binario_para_decimal():
    binario = entrada.get()
    try:
        decimal = int(binario, 2)
        resultado.config(text=f"{decimal}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número binário válido.")

def decimal_para_binario():
    decimal = entrada.get()
    try:
        decimal_int = int(decimal)
        binario = bin(decimal_int)[2:]
        resultado.config(text=f"{binario}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número decimal válido.")

# Campo de Entrada
entrada = tk.Entry(
    janela, 
    width=25,
    font=('Arial', 18),
    bg="#8E7BEF",
    fg='white',
    relief='flat',
    bd=0,
    highlightthickness=4,
    highlightbackground="#A29BFE",
    highlightcolor="#DCD6F7",
    insertbackground='white',
    justify='center'
)
entrada.pack(padx=30, pady=25)

# Estilo de botões
btn_style = {
    'font': ('Verdana', 12, 'bold'),
    'bg': '#4C3DB2',
    'fg': 'white',
    'activebackground': '#6C5CE7',
    'activeforeground': 'white',
    'bd': 0,
    'relief': 'flat',
    'width': 20,
    'height': 2,
    'cursor': 'hand2'
}

# Botão de Binário para Decimal
btn_bin_dec = tk.Button(janela, text="Binário → Decimal", command=binario_para_decimal, **btn_style)
btn_bin_dec.pack(pady=10)

# Botão de Decimal para Binário
btn_dec_bin = tk.Button(janela, text="Decimal → Binário", command=decimal_para_binario, **btn_style)
btn_dec_bin.pack(pady=10)

# Resultado
resultado = tk.Label(
    janela, 
    text="", 
    font=("Verdana", 16, 'bold'), 
    fg="white", 
    bg="#8E7BEF", 
    width=25, 
    height=2,
    relief='flat'
)
resultado.pack(pady=30)

# Rodapé
rodape = tk.Label(
    janela,
    text="Desenvolvido por Laura Cordeiro",
    font=('Arial', 10),
    bg='#6C63FF',
    fg='white'
)
rodape.pack(side='bottom', pady=10)

# Loop
janela.mainloop()
