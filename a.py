import tkinter as tk
from tkinter import messagebox
import os

def calcular_imc():
    user_name = entry_nome.get()
    idade = int(entry_idade.get())
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())

    imc = peso / (altura * altura)

    messagebox.showinfo("Resultado", f"{user_name}, seu IMC é: {imc:.2f}")

    if imc < 16.9:
        messagebox.showinfo("Classificação", "Muito baixo do peso")
    elif imc < 18.4:
        messagebox.showinfo("Classificação", "Baixo do peso")
    elif imc < 24.9:
        messagebox.showinfo("Classificação", "Peso Normal")
    elif imc < 29.9:
        messagebox.showinfo("Classificação", "Acima do peso")
    elif imc < 34.9:
        messagebox.showinfo("Classificação", "Obesidade grau I")
    elif imc < 40:
        messagebox.showinfo("Classificação", "Obesidade grau II")
    else:
        messagebox.showinfo("Classificação", "Obesidade grau III")

    # Limpar os campos de entrada
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)

# Criando a janela
#root = tk.Tk()
#root.title("Calculadora de IMC")

# Crie a janela
root = tk.Tk()
root.title("Calculadora de IMC")

largura = 500
altura = 330
posx = (root.winfo_screenwidth() - largura) // 2
posy = (root.winfo_screenheight() - altura) // 2
root.geometry(f"{largura}x{altura}+{posx}+{posy}")

# Criando o frame principal
frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Criando os widgets
label_nome = tk.Label(frame, text="Nome:")
entry_nome = tk.Entry(frame)

label_idade = tk.Label(frame, text="Idade:")
entry_idade = tk.Entry(frame)

label_peso = tk.Label(frame, text="Peso (KG):")
entry_peso = tk.Entry(frame)

label_altura = tk.Label(frame, text="Altura (m):")
entry_altura = tk.Entry(frame)

button_calcular = tk.Button(frame, text="Calcular IMC", command=calcular_imc, bg='lightgray')

# Posicionando os widgets no frame usando pack
label_nome.pack(side=tk.TOP, fill=tk.X, pady=5)
entry_nome.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

label_idade.pack(side=tk.TOP, fill=tk.X, pady=5)
entry_idade.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

label_peso.pack(side=tk.TOP, fill=tk.X, pady=5)
entry_peso.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

label_altura.pack(side=tk.TOP, fill=tk.X, pady=5)
entry_altura.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

button_calcular.pack(side=tk.TOP, fill=tk.X, pady=10)

# Rodando a aplicação
root.mainloop()
