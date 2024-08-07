import flet as ft


def clicando_botao_arquivo(e):
    print("Clicou!!!!")


# criando os elementos
def salvar_arquivo_texto(caixa_texto, pagina):
    # nome_arquivo_texto
    with open('times.txt', 'w', encoding='utf-8') as arquivo_texto:
        nome_arquivo = arquivo_texto.name
        print(nome_arquivo)
        arquivo_texto.write(caixa_texto.value)
        pagina.update()


def limpar_caixa_texto(caixa_texto, pagina):
    caixa_texto.value = ""
    pagina.title = "Bloco de Notas"
    pagina.update()


def abrir_arquivo(caixa_texto, pagina, x):
    caminho = str(x.path)
    arquivo = str(x.name)
    with open(caminho, 'r+') as arquivo_texto:
        caixa_texto.value = arquivo_texto.read()
        pagina.update()









def fechar_janela(pagina):
    pass


def titulo_pagina_arquivo_texto(nome_arquivo_texto, pagina):
    pagina.title = f"{nome_arquivo_texto}-Bloco de Notas"
    pagina.update()
