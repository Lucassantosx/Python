# CRIAR BANCO DE DADOS

import sqlite3

conexao = sqlite3.connect('UsuariosData.db') # REALIZANDO A CONEXÃO

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuarios (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Usuario TEXT NOT NULL,
    Senha TEXT NOT NULL

);
""") #EXECUTAR UM COMANDO SQL

print("Conectado ao Banco de Dados")

#cursor.execute("""
#INSERT INTO Usuarios VALUES ('Lucas Xavier','lucasmsxavier@hotmail.com','LucasSantosX','Luna1002')
#""") # INSERINDO DADOS NA TABELA

