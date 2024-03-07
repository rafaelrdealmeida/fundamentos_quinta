from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
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
    #     #button1[

    data = anos[5].click()
    sleep (2)
    botao_pesquisar = navegador.find_element(By.CSS_SELECTOR,"#button1").click()
    sleep (2)

    # for i in range(0,10):

    #     data = anos[i].click()
    #     sleep (2)
    #     botao_pesquisar = navegador.find_element(By.CSS_SELECTOR,"#button1").click()
    #     sleep (2)

    # for ano in anos[-3:-1]:
    #     data = ano.click()
    #     sleep (2)
    #     botao_pesquisar = navegador.find_element(By.CSS_SELECTOR, "#button1").click()
    #     sleep(2)
    #     print("fim")





    # for tag_ano in anos:

    #     data = anos[2].click()
    #     sleep(10)
    #     botao_pesquisar = navegador.find_element(By.CSS_SELECTOR, "#button1").click()
    #     sleep(2)
       
    # # clicar em pesquisar
   





def main():
    link = "https://imagem.camara.leg.br/pesquisa_diario_basica.asp"
    acessar_pagina_dinamica(link)
    
    

if __name__ == "__main__":
    main()