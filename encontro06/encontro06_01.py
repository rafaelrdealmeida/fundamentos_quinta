import requests
import urllib.request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#TODO: qual ferramenta utilizar para a coleta (beautifulsoap ou selenium)?
#TODO: pagina estática VS página dinamica
#TODO: webscraping com selenium
#TODO: analise dos dados


def acessar_pagina_dinamica(link):
    # emulador de navegador
    navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
            ##########
            # Coletando link com o requests
            ##########
            
            # # Obtenha o URL da página atual (após redirecionamento, se houver)
            link = navegador.current_url
            
            # Baixe o PDF
            # urllib.request.urlretrieve(link,  f'{data_formatada}.pdf')
            pdf = requests.get(link)
            # http://Imagem.camara.gov.br/Imagem/d/pdf/DCD0020240125000010000.PDF#page=
            # [http://Imagem.camara.gov.br/Imagem/d/pdf/DCD0020240125000010000.PDF,page=]
            link_pdf = link.split("#")[0]
            print(link_pdf)
            with open( f'{data_formatada}.pdf', 'wb') as f:
                f.write(link_pdf.content)

        contador = contador + 1
        sleep(2)

def pegar_pdfs():
    # <td class="calWeekDaySel"><a class="WeekDay" href="dc_20b.asp?selCodColecaoCsv=D&amp;Datain=5/2/2019">5</a></td> 
    # <td class="calWeekEndSel"><a class="WeekEnd" href="dc_20b.asp?selCodColecaoCsv=D&amp;Datain=9/2/2019">9 </a></td>
    pass   

def main():
    link = "https://imagem.camara.leg.br/pesquisa_diario_basica.asp"
    acessar_pagina_dinamica(link)
    
    

if __name__ == "__main__":
    main()