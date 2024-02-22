import requests
from bs4 import BeautifulSoup
# import pandas as pd


def acessar_pagina(link):
    """responsável por acessar as paginas da internet"""
    pagina = requests.get(link)
    bs = BeautifulSoup(pagina.text, "html.parser")
    return bs 

def extrair_infos():
    """responsavel por extrair as informações das paginas"""
    link= "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int=0"
    pagina =  acessar_pagina(link)
    # <div id="content-core">
    lista_notas = pagina.find("div", attrs={"id":"content-core"}).find_all("article")
    print(len(lista_notas))
    for nota in lista_notas:
        # titulo
        # numero_nota (só numero)
        # link
        # data
        # horario
        titulo = nota.h2.text.strip()
        link = nota.a["href"]
        print(titulo)
        print(link)
        print("#####")






def main():
    coletar_dados = extrair_infos()


if __name__ == "__main__":
    main()