import json
import requests
import urllib.request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#TODO: qual ferramenta utilizar para a coleta (beautifulsoap ou selenium)? - ok
#TODO: pagina estática VS página dinamica - ok
#TODO: webscraping com selenium - ok
#TODO: analise dos dados


def acessar_pagina_dinamica(link):
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage') 
    # emulador de navegador
    navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    # acessar a página
    navegador.get(link)
    sleep(2)
    contador = 0
    while contador < 14:
        anos = navegador.find_element(By.CSS_SELECTOR, "#ano").find_elements(By.TAG_NAME, "option") #["2024", "2023", "2022"...]
        anos[contador].click() # clica no ano
        navegador.find_element(By.CSS_SELECTOR,"#button1").click() # clica no botão pesquisar
        ## pegar_pdfs
        dias = navegador.find_elements(By.CSS_SELECTOR, ".calWeekDaySel, .calWeekEndSel") #["dia1", "dia2"]
        
        print(len(dias))
        # <td class="calWeekDaySel"><a class="WeekDay" href="dc_20b.asp?selCodColecaoCsv=D&amp;Datain=5/2/2019">5</a></td> 
        for dia in dias:
            # Obtenha o valor do atributo href
            tag_a = dia.find_element(By.TAG_NAME, "a")
            atributo_href = tag_a.get_attribute("href")
            print(atributo_href)
            ####################
            # nome do arquivo
            ###################
            # String de data no formato "dd/mm/yyyy"
            # https://imagem.camara.leg.br/dc_20b.asp?selCodColecaoCsv=D&Datain=22/12/2018
            # ["https://imagem.camara.leg.br/dc_20b.asp?selCodColecaoCsv","D&Datain","22/12/2018"]
            data_string = atributo_href.split("=")[-1]
            # Converter para objeto datetime
            data_objeto = datetime.strptime(data_string, "%d/%m/%Y")
            # Formatar para o formato "yyyy-mm-dd"
            data_formatada = data_objeto.strftime("%Y-%m-%d")
            # "dc_20b.asp?selCodColecaoCsv=D&amp;Datain=6/2/2024"
            # https://imagem.camara.leg.br/montaPdf.asp?narquivo=DCD0020240206000020000.PDF&npagina=
            # https://imagem.camara.gov.br/Imagem/d/pdf/DCD0020240206000020000.PDF#page=
            pdf = obter_url_final_apos_redirecionamentos(atributo_href)
            
            resposta = requests.get(pdf)
    
            # Verifique se a solicitação foi bem-sucedida (status code 200)
            if resposta.status_code == 200:
                # Salve o conteúdo do PDF em um arquivo local
                with open(f"{data_formatada}.pdf", 'wb') as f:
                    f.write(resposta.content)
                print("PDF baixado com sucesso!")
            else:
                print(f"Não foi possível baixar o PDF. Status code: {resposta.status_code}")
        contador = contador + 1
        sleep(2)

# URL final do PDF
                    
def obter_url_final_apos_redirecionamentos(url_link):
    """"responsavel por acompanhar todos os redirecionamentos até chegar no arquivo .pdf"""
    # Inicialize o navegador
    # url_link =  # "dc_20b.asp?selCodColecaoCsv=D&amp;Datain=6/2/2024"
    # "dc_20b.asp?selCodColecaoCsv=D&amp;Datain=6/2/2024"
    # https://imagem.camara.leg.br/montaPdf.asp?narquivo=DCD0020240206000020000.PDF&npagina=
    # https://imagem.camara.gov.br/Imagem/d/pdf/DCD0020240206000020000.PDF#page=
    navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # Faça uma solicitação GET para obter a URL final após os redirecionamentos
    navegador.get(url_link)
    
    # Obtenha a URL inicial
    url_redirecionamento = navegador.current_url # https://imagem.camara.leg.br/montaPdf.asp?narquivo=DCD0020240206000020000.PDF&npagina=
    
    # Repita o processo até que não haja mais redirecionamentos
    while True:
        # Aguarde um segundo para garantir que a página seja carregada completamente
        sleep(1)
        
        # Obtenha a URL atual
        url_atual = navegador.current_url # https://imagem.camara.gov.br/Imagem/d/pdf/DCD0020240206000020000.PDF#page=
        
        # Se a URL atual for diferente da anterior, atualize a URL anterior e continue o loop
        if url_atual != url_redirecionamento:
            url_redirecionamento   = url_atual
            continue
        else:
            # Se não houver mais redirecionamentos, retorne a URL final e feche o navegador
            navegador.quit()
            return url_atual

                

def pegar_pdfs():
    # <td class="calWeekDaySel"><a class="WeekDay" href="dc_20b.asp?selCodColecaoCsv=D&amp;Datain=5/2/2019">5</a></td> 
    # <td class="calWeekEndSel"><a class="WeekEnd" href="dc_20b.asp?selCodColecaoCsv=D&amp;Datain=9/2/2019">9 </a></td>
    pass   

def main():
    link = "https://imagem.camara.leg.br/pesquisa_diario_basica.asp"
    acessar_pagina_dinamica(link)
    
    

if __name__ == "__main__":
    main()