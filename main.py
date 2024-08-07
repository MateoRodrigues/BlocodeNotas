import flet as ft
import os
import editar


def principal(pagina: ft.Page):
    #importando bibliotecas
    import arquivo
    import editar
    import exibir
    pagina.title = "Bloco de Notas"
    pagina.vertical_alignment = ft.MainAxisAlignment.START
    pagina.window_height = 800
    pagina.window_width = 800
    pagina.spacing = 0
    pagina.padding = 0
    exibir.tema(pagina)
    # Caixa de texto
    caixa_texto = ft.TextField(
        multiline=True,
        expand=True,
        min_lines=10,
        max_lines=None,
        border=ft.InputBorder.NONE,
    )

    def funcao_abrir_explorador(e: ft.FilePickerResultEvent):
        for x in e.files:
            arquivo.abrir_arquivo(caixa_texto, pagina, x)
            nome_arquivo = str(x.name)
            arquivo.titulo_pagina_arquivo_texto(nome_arquivo, pagina)
    def salvar_como_arquivo(e: ft.FilePickerResultEvent):
        pasta = e.path
        def retorna_nome_criado():
            for x in e.files:
                return x.name
        nome_arquivo_criado = retorna_nome_criado()
        novo_arquivo = os.path.join(pasta,nome_arquivo_criado)
        with open(novo_arquivo, 'w', enconding='utf-8') as arquivo_texto:
            arquivo_texto.write(caixa_texto.value)

    salvar_como = ft.FilePicker(on_result=salvar_como_arquivo)
    pagina.overlay.append(salvar_como)
    abrir_arquivo = ft.FilePicker(on_result=funcao_abrir_explorador)
    pagina.overlay.append(abrir_arquivo)
    #botões
    botao_arquivo = ft.SubmenuButton(content=ft.Text("Arquivo"),
                    controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Novo"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                        on_click=lambda e: arquivo.limpar_caixa_texto(caixa_texto, pagina)
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Abrir"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                        on_click=lambda e: abrir_arquivo.pick_files()
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Salvar"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                        on_click=lambda e: arquivo.salvar_arquivo_texto(caixa_texto,pagina)
                    ),
                    ft.MenuItemButton(
                            content=ft.Text("Salvar Como"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                        on_click=lambda e: salvar_como.save_file()
                        ),
                    ft.MenuItemButton(
                            content=ft.Text("Sair"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                        on_click= lambda e: arquivo.fechar_janela(pagina)
                        )
            ]
    )





    botao_editar = ft.SubmenuButton(content=ft.Text("Editar"),
                    controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Desfazer"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Recortar"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Copiar"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Colar"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                    ),
                    ft.MenuItemButton(
                            content=ft.Text("Excluir"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                        ),
                    ft.MenuItemButton(
                            content=ft.Text("Substituir"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Selecionar tudo"),
                            style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                        ),
                        ft.MenuItemButton(
                            content=ft.Text(r"Hora\\data"),
                            style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                            on_click=lambda e: editar.hora_data_atual(caixa_texto, pagina)
                        )
            ]
    )
    botao_formatar = ft.SubmenuButton(content=ft.Text("Formatar"),
                    controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Quebra automática da linha"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Fonte..."),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                    )

            ]
    )
    botao_exibir =  ft.SubmenuButton(content=ft.Text("Exibir"),
                    controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Zoom"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Barra de Status"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                    ),
                    ft.SubmenuButton(
                            content=ft.Text("Tema"),
                            style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                            controls=[ft.MenuItemButton(
                                content=ft.Text("Claro"),
                                leading=ft.Icon(ft.icons.LIGHT_MODE),
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                                on_click=lambda e: exibir.mudar_tema_claro(pagina)
                            ), ft.MenuItemButton(
                                content=ft.Text("Escuro"),
                                leading=ft.Icon(ft.icons.DARK_MODE),
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                                on_click= lambda e: exibir.mudar_tema_escuro(pagina)
                            )]
                        )

            ]
    )

    # Define uma linha separadora sem bordas improvisado
    divisor = ft.Container(
        height=1,
        bgcolor=ft.colors.WHITE,  # Cor da linha
        border_radius=0  # Remove arredondamento
    )
    menubar = ft.MenuBar(expand=True,controls=[botao_arquivo,botao_editar,botao_formatar,botao_exibir])
    #adicionando a pagina
    pagina.add(ft.Row([menubar]))
    pagina.add(divisor)
    pagina.add(ft.Row([caixa_texto],alignment=ft.MainAxisAlignment.END))



ft.app(target=principal)
