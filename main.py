import flet as ft

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
    # Caixa de texto
    caixa_texto = ft.TextField(
        multiline=True,
        expand=True,
        min_lines=10,
        max_lines=None,
        border=ft.InputBorder.NONE,
    )
    salvar_como = ft.FilePicker(on_result=arquivo.salvar_como_arquivo)
    pagina.overlay.append(salvar_como)
    abrir = ft.FilePicker(on_result=arquivo.abrir_arquivo(caixa_texto=caixa_texto, pagina=pagina))
    pagina.overlay.append(abrir)
    #botões
    botao_arquivo = ft.SubmenuButton(content=ft.Text("Arquivo"),
                    controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Novo"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                        on_click=lambda e: arquivo.limpar_caixa_texto(caixa_texto, pagina)
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Nova janela"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE})
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Abrir"),
                        style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                        on_click=lambda e: abrir.pick_files()
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
                                style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.BLUE}),
                                on_click=lambda e: exibir.mudar_tema_claro(pagina)
                            ), ft.MenuItemButton(
                                content=ft.Text("Escuro"),
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

    #adicionando a pagina
    pagina.add(ft.Row([botao_arquivo,botao_editar,botao_formatar,botao_exibir], alignment=ft.MainAxisAlignment.START,spacing=0))
    pagina.add(divisor)
    pagina.add(ft.Row([caixa_texto],alignment=ft.MainAxisAlignment.END))



ft.app(target=principal)
