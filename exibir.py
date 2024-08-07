'''def mudar_tema_claro(pagina):
    pagina.theme_mode = "light"
    tema(pagina)
    pagina.update()

def mudar_tema_escuro(pagina):
    pagina.theme_mode = "dark"
    pagina.update()


def tema(pagina):
    pass'''

import csv
with open("tema.csv", "w+", newline='') as tema_arquivo:
     escrever_csv = csv.writer(tema_arquivo)
     escrever_csv.writerow(['Tema'])