# importar as bibliotecas

from tkinter import *
#from tkinter import messagebox
from tkinter import ttk

# Criar nossa Janela

jan = Tk()
jan.title("Lucas Systems - Painel de Acesso")
jan.geometry("600x400")
jan.configure(background="white")
jan.resizable(width=False, height=False) #impede de mexer na tela
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="imagens/login.ico") #adicionar o ícone

#====== CARREGANDO IMAGENS ===========

logo = PhotoImage(file="imagens/logo.png")

#========= WIDGETS =============
LeftFrame = Frame(jan, width=200, height=400, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=400, bg="MIDNIGHTBLUE", relief="raise" )
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Usuário: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5,y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5 , y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="**********")
PassEntry.place(x=150, y=160)

# BOTÕES

LoginBotao = ttk.Button(RightFrame, text="Login", width=30)
LoginBotao.place(x=100, y=225)

def Registro():

# REMOVENDO WIDGETS DE LOGIN
  LoginBotao.place(x=5000) # fazer o botão sumir
  RegistroBotao.place (x=5000)


# INSERINDO WIDGETS DE CADASTRO

  NomeLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
  NomeLabel.place(x=5, y=5)
  NomeEntry = Entry(RightFrame, width=39)
  NomeEntry.place(x=100, y=18)

  EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
  EmailLabel.place(x=5,y=55)
  EmailEntry = Entry(RightFrame,width=39)
  EmailEntry.place(x=100, y=68)

  RegisterBotao = ttk.Button(RightFrame, text="Salvar", width=20)
  RegisterBotao.place(x=50, y=260)

  def VoltarLogin ():
#REMOVENDO WIDGETS DE CADASTRO

     NomeLabel.place(x=5000)
     NomeEntry.place(x=5000)
     EmailLabel.place(x=5000)
     EmailEntry.place(x=5000)
     RegisterBotao.place(x=5000)
     VoltarBotao.place(x=5000)

# RETORNANDO WIDGETS DE LOGIN
     LoginBotao.place(x=100, y=225)
     RegistroBotao.place(x=130, y=260)

  VoltarBotao = ttk.Button(RightFrame, text="Voltar", width=20, command=VoltarLogin)
  VoltarBotao.place(x=200, y=260)

RegistroBotao = ttk.Button(RightFrame, text="Registro", width=20, command=Registro)
RegistroBotao.place(x=130, y=260)

jan.mainloop()
