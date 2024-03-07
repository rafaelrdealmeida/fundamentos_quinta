import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
# import pandas as pd

#TODO: extrair as informações: numero da nota-ok, titulo-ok, link-ok, data-ok, horario-ok
#TODO: percorrer todas as paginas - ok
#TODO: extrair o conteúdo (paragrafos, horario e data atualização) de cada link -ok
#TODO: inserir as informações em um arquivo JSON - ok


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
            
            # caso 1 >>> "Número de nota é: 150" ["Número","de", "nota","é:","150"]
            # caso 2 >>> None
            # caso 3 >>> ["Número","de", "nota","é:","15/1997"]["15","1997"]
            
            try:
                numero = nota.find("span", attrs={"class": "subtitle"}).text.strip().split()[-1] # caso 1
                numero = numero.split("/")[0] # caso 3
            except AttributeError as erro:
                if str(erro) == "'NoneType' object has no attribute 'text'":
                    numero = "NA" # caso 2
            
            # outro jeito de resolver o caso 3
            # if numero != "NA" :
            #     verificar = numero.find("/")
            #     # 15/1997 >> ["15", "1997"]
            #     print(f"VERIFICAR: {verificar}")
            #     if verificar != -1:
            #         numero = numero.split("/")[0] # caso 3

            # "summary-view-icon"
            data = nota.find_all("span", attrs={"class":"summary-view-icon"})[0].text.strip()
            horario = nota.find_all("span", attrs={"class":"summary-view-icon"})[1].text.strip()
            # extrair paragrafos e data e horario de atualização
            
            print(titulo)
            print(link)
            print(f"Número de nota é: {numero}")
            print(data)
            print(horario)

            conteudo = acessar_pagina(link)
            # class="documentModified"
            tag_span = conteudo.find("span", attrs={"class": "documentModified"}).find("span", attrs={"class": "value"}).text.strip()
            data_atualizada = tag_span.split()[0]
            horario_atualizado = tag_span.split()[1]

            print(data_atualizada)
            print(horario_atualizado)
            lista_tag_p = conteudo.find("div", attrs={"property":"rnews:articleBody"}).find_all("p")
            paragrafos = []
            for paragrafo in lista_tag_p:
                paragrafos.append(paragrafo.text.strip())
            print(paragrafos)

            inserir_bd(titulo, link, data, horario,data_atualizada, horario_atualizado,paragrafos)

            print("#####")

def acessar_pagina(link):
    """responsável por acessar as paginas da internet"""
    pagina = requests.get(link)
    bs = BeautifulSoup(pagina.text, "html.parser")
    return bs 

def percorrer_paginas(url_base):
    # https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int=60
    # são 5040 notas e cada pagina tem 30 notas
    lista_de_links = []
    contador = 5010
    while contador >= 0:
        link = url_base + str(contador)
        lista_de_links.append(link)
        contador = contador - 30
        
    return lista_de_links

def inserir_bd(titulo, link, data, horario,data_atualizada, horario_atualizado,paragrafos):
    """responsavel por criar o banco json"""
    bd = TinyDB ("notas_mre.json", indent=4, ensure_ascii=False)
    buscar = Query()
    verificar_bd = bd.contains(buscar.link == link) # True ou False
    if not verificar_bd:
        print(f"Não esta no banco json. Inserindo...verifica_bd é {verificar_bd}")
        bd.insert(
            {
            "titulo": titulo, 
            "link": link, 
            "data": data,
            "horario": horario,
            "data_atualizada": data_atualizada,
            "horario_atualizado": horario_atualizado,
            "paragrafos":paragrafos 
            }
        )
    else:
        print(f"Já está no banco. Não será inseirdo novamente... verifica_bd é {verificar_bd}")



def main():
    url_base = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int="
    lista_links = percorrer_paginas(url_base)
    extrair_infos(lista_links)

    # coletar_dados = extrair_infos()
    

if __name__ == "__main__":
    main()