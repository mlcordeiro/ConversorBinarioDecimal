import tkinter as tk
from tkinter import messagebox

# Janela 
janela = tk.Tk()
janela.title('Calculadora Binário-Decimal')
janela.geometry('400x500')
janela.configure(bg="#1E1E2F")  # Fundo escuro

# Título
titulo = tk.Label(
    janela,
    text='Calculadora Binário - Decimal',
    font=('Helvetica', 18, 'bold'),
    bg='#1E1E2F',
    fg='#F8F8F2'
)
titulo.pack(padx=20, pady=30)

# Funções
def binario_para_decimal():
    binario = entrada.get()
    try:
        decimal = int(binario, 2)
        resultado.config(text=f"Decimal: {decimal}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número binário válido.")

def decimal_para_binario():
    decimal = entrada.get()
    try:
        decimal_int = int(decimal)
        binario = bin(decimal_int)[2:]
        resultado.config(text=f"Binário: {binario}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número decimal válido.")

# Entrada
entrada = tk.Entry(
    janela, 
    width=25,
    font=('Helvetica', 16),
    bg="#2E2E3E",
    fg='#F8F8F2',
    relief='flat',
    bd=0,
    highlightthickness=4,
    highlightbackground="#5A5A89",
    highlightcolor="#8A8AC9",
    insertbackground='#F8F8F2',
    justify='center'
)
entrada.pack(padx=30, pady=25)

# Botões
btn_style = {
    'font': ('Helvetica', 12, 'bold'),
    'bg': '#5A5A89',
    'fg': '#F8F8F2',
    'activebackground': '#8A8AC9',
    'activeforeground': '#F8F8F2',
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
    font=("Helvetica", 16, 'bold'), 
    fg="#F8F8F2", 
    bg="#2E2E3E", 
    width=30, 
    height=2,
    relief='flat',
    bd=0
)
resultado.pack(pady=30)

# Rodapé
rodape = tk.Label(
    janela,
    text="Desenvolvido por Laura Cordeiro",
    font=('Helvetica', 10),
    bg='#1E1E2F',
    fg='#555'
)
rodape.pack(side='bottom', pady=10)

# Loop
janela.mainloop()
