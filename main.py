import tkinter as tk
from tkinter import *
import os
from time import strftime
import pyttsx3

root = tk.Tk()
root.title('Otaku!!')
root.geometry("600x380")
root.maxsize(600, 380)
root.minsize(600, 380)
root.configure(background='#1d1d1d')

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    speak('São ' + hora_atual)
    root.after(1000, get_horas)

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text='Olá, ' + nome_usuario)
    speak('Olá, ' + nome_usuario)

def get_data():
    data_atual = strftime('%d/%m/%Y')
    data.config(text=data_atual)
    speak('Hoje é ' + data_atual)

tela = tk.Canvas(root, width=600, height=60, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
tela.pack()
saudacao = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 17))
saudacao.pack()
data = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 15))
data.pack(pady=2)
horas = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Montserrat', 65))
horas.pack(pady=2)

# Chamando as funções após a definição delas
get_saudacao()
get_data()
get_horas()

root.mainloop()
