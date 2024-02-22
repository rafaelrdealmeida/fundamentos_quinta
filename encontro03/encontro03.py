import requests
from bs4 import BeautifulSoup
# import pandas as pd

#TODO: extrair as informações: numero da nota-ok, titulo-ok, link-ok, data-ok, horario-ok
#TODO: percorrer todas as paginas - ok
#TODO: extrair o conteúdo (paragrafos) de cada link
#TODO: inserir as informações em um arquivo JSON
#TODO: webscraping com selenium

# if name e def main
# o que é uma função e como é sua estrutura (return e chamada de função)
# o que é uma variável
# tipos de dados (numeros inteiros, decimais/float, string e listas )
# loop for
# metods de string - strip(),split()
# indices de lista
# conversão de numero inteiro para string
# loop while
# metod de lista - append()
# try e except

def acessar_pagina(link):
    """responsável por acessar as paginas da internet"""
    pagina = requests.get(link)
    bs = BeautifulSoup(pagina.text, "html.parser")
    return bs 

def extrair_infos(lista_links):
    """responsavel por extrair as informações das paginas"""
    for link in lista_links:
        pagina =  acessar_pagina(link)
        # find (encontra um elemento ou delimitar um pedaço da pagina)
        # find_all (encontra uma  lista de elementos) [elemento01, elemento02, elemento03]
        lista_notas = pagina.find("div", attrs={"id":"content-core"}).find_all("article")
        # print(lista_notas, len(lista_notas))
        for nota in lista_notas:
            # data
            # horario
            titulo = nota.h2.text.strip()
            link = nota.a["href"]
            # span class="subtitle"
            try:
                numero = nota.find("span", attrs={"class": "subtitle"}).text.strip().split()[-1]
            except AttributeError as erro:
                if str(erro) == "'NoneType' object has no attribute 'text'":
                    numero = "NA"
            # "summary-view-icon"
            data = nota.find_all("span", attrs={"class":"summary-view-icon"})[0].text.strip()
            horario = nota.find_all("span", attrs={"class":"summary-view-icon"})[1].text.strip()
            # extrair paragrafos e data e horario de atualização
            
            print(titulo)
            print(link)
            print(f"Número de nota é: {numero}")
            print(data)
            print(horario)
            print("#####")

def percorrer_paginas(url_base):
    # https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int=60
    # são 5040 notas e cada pagina tem 30 notas
    lista_de_links = []
    contador = 5010
    while contador >= 0:
        link = url_base + str(contador)
        contador = contador - 30
        lista_de_links.append(link)
    return lista_de_links



def main():
    url_base = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int="
    lista_links = percorrer_paginas(url_base)
    extrair_infos(lista_links)

    # coletar_dados = extrair_infos()
    



if __name__ == "__main__":
    main()