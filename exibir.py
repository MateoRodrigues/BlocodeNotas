def mudar_tema_claro(pagina):
    pagina.theme_mode = "light"
    import csv
    with open('tema.csv', 'r+') as arquivo_csv:
        tema = ["Tema"]
        escrever_csv = csv.DictWriter(arquivo_csv,tema)
        escrever_csv.writeheader()
        escrever_csv.writerow({'Tema': "light"})
    pagina.update()

def mudar_tema_escuro(pagina):
    pagina.theme_mode = "dark"
    import csv
    with open('tema.csv', 'r+') as arquivo_csv:
        tema = ["Tema"]
        escrever_csv = csv.DictWriter(arquivo_csv,tema)
        escrever_csv.writeheader()
        escrever_csv.writerow({'Tema':'dark'})
    pagina.update()


def tema(pagina):
     import csv
     with open('tema.csv', newline='') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             pagina.theme_mode = row['Tema']
