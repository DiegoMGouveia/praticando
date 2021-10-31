#  codigo com funções de conexão de banco de dados sqlite.
#  banco de dados para armazenar dados importantes, como informações dos clientes e seus veiculos.

import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    caminho = "/media/diego/EA00FB8D00FB5F4F/python3 projetos/lojacarros/basededadosoficina.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = ConexaoBanco()

vsql = '''CREATE TABLE clientesdb(
            NOME VARCHAR,
            CONTATO VARCHAR,
            ENDERECO VARCHAR,
            PLACA VARCHAR,
            MODELO VARCHAR,
            COR VARCHAR,
            ANO VARCHAR,
            TIPODESERVICO VARCHAR,
            OBERVACAO VARCHAR,
            CUSTO VARCHAR,
            PAGO VARCHAR
        );'''

def CriarTabela(conexao,sql):
        try:
            c=conexao.cursor()
            c.execute(sql)
            print('tabela criada!')
        except Error as ex:
            print(ex)


CriarTabela(vcon, vsql)


vcon.close()

