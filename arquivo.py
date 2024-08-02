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


def abrir_arquivo(caixa_texto, pagina,x):
    caminho = str(x.path)
    arquivo = str(x.name)
    with open(caminho, 'r+') as arquivo_texto:
        caixa_texto.value = arquivo_texto.read()
        pagina.update()

def abrir_explorador(e: ft.FilePickerResultEvent,caixa_texto,pagina):
    for x in e.files:
        abrir_arquivo(caixa_texto,pagina,x)
        nome_arquivo = str(x.name)
        titulo_pagina_arquivo_texto(nome_arquivo,pagina)
def salvar_como_arquivo(e:ft.FilePickerResultEvent):
    salve_localizacao = e.path
    if salve_localizacao:
        try:
            with open(salve_localizacao, 'w', enconding='utf-8') as arquivo_texto:
                print('Sucesso!')
        except Exception as erro:
            print("ERRO:", erro)

"""def nova_janela(pagina):
    pagina.page()
    pagina.update()"""
def fechar_janela(pagina):
    pass

def titulo_pagina_arquivo_texto(nome_arquivo_texto,pagina):
    pagina.title = f"{nome_arquivo_texto}-Bloco de Notas"
    pagina.update()

