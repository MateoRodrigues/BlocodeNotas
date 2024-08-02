
def hora_data_atual(caixa_texto,pagina):
    from datetime import datetime
    data_atual = datetime.now()
    string_data_atual = str(data_atual.strftime("%H:%M %d/%m/%Y"))
    caixa_texto.value += string_data_atual
    pagina.update()
#def substituir_palavra(caixa_texto,pagina):

