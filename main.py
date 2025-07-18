import tkinter as tk
from tkinter import messagebox
from validate_docbr import CPF, CNPJ

# Função para validar CPF ou CNPJ
def validar_documento():
    tipo = var_tipo.get()
    numero = entry_documento.get().strip()

    if tipo == "CPF":
        cpf = CPF()
        if cpf.validate(numero):
            messagebox.showinfo("Resultado", "✅ CPF válido!")
        else:
            messagebox.showerror("Erro", "❌ CPF inválido!")
    elif tipo == "CNPJ":
        cnpj = CNPJ()
        if cnpj.validate(numero):
            messagebox.showinfo("Resultado", "✅ CNPJ válido!")
        else:
            messagebox.showerror("Erro", "❌ CNPJ inválido!")
    else:
        messagebox.showwarning("Atenção", "Selecione CPF ou CNPJ.")

# Interface
janela = tk.Tk()
janela.title("Validador de CPF/CNPJ")
janela.geometry("350x220")
janela.configure(bg="#d9fcd9")  # Cor esverdeada clara

# Título
titulo = tk.Label(janela, text="Validação de CPF ou CNPJ", font=("Arial", 14, "bold"), bg="#d9fcd9", fg="#2d6a4f")
titulo.pack(pady=10)

# Seleção CPF/CNPJ
var_tipo = tk.StringVar()

frame_opcoes = tk.Frame(janela, bg="#d9fcd9")
frame_opcoes.pack(pady=5)

rb_cpf = tk.Radiobutton(frame_opcoes, text="CPF", variable=var_tipo, value="CPF", bg="#d9fcd9", fg="#1b4332", font=("Arial", 11))
rb_cpf.pack(side="left", padx=10)

rb_cnpj = tk.Radiobutton(frame_opcoes, text="CNPJ", variable=var_tipo, value="CNPJ", bg="#d9fcd9", fg="#1b4332", font=("Arial", 11))
rb_cnpj.pack(side="left", padx=10)

# Campo para digitar
label_documento = tk.Label(janela, text="Digite o número:", bg="#d9fcd9", fg="#081c15", font=("Arial", 11))
label_documento.pack(pady=5)

entry_documento = tk.Entry(janela, font=("Arial", 12), width=25)
entry_documento.pack()

# Botão validar
btn_validar = tk.Button(janela, text="Validar", command=validar_documento, bg="#95d5b2", fg="black", font=("Arial", 12, "bold"))
btn_validar.pack(pady=15)

janela.mainloop()
