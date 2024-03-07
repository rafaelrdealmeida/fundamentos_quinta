from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


#TODO: webscraping com selenium
#TODO: analise dos dados


def acessar_pagina_dinamica(link):
    # emulador de navegador
    navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # acessar a página
    navegador.get(link)
    sleep(2)
    # selecionar o ano
    tag_anos = navegador.find_element(By.CSS_SELECTOR, "#ano").find_elements(By.TAG_NAME, "option")
    anos = []
    for tag_ano in tag_anos:
        ano = tag_ano
        anos.append(ano)

    contador = 0
    while contador < 30:
        encontrar = navegador.find_element(By.CSS_SELECTOR, "#ano").find_elements(By.TAG_NAME, "option")
        encontrar[contador].click()
        navegador.find_element(By.CSS_SELECTOR,"#button1").click()
        contador = contador + 1
        sleep(2)

        
    





def main():
    link = "https://imagem.camara.leg.br/pesquisa_diario_basica.asp"
    acessar_pagina_dinamica(link)
    
    

if __name__ == "__main__":
    main()