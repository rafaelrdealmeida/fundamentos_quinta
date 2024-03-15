import requests

# URL do PDF
url_pdf = "https://imagem.camara.gov.br/Imagem/d/pdf/DCD0020190101000010000.PDF"

# Nome do arquivo onde o PDF será salvo
nome_arquivo = "arquivo.pdf"

# Faça o download do PDF
resposta = requests.get(url_pdf)

# Verifique se a solicitação foi bem-sucedida (status code 200)
if resposta.status_code == 200:
    # Salve o conteúdo do PDF em um arquivo local
    with open(nome_arquivo, 'wb') as f:
        f.write(resposta.content)
    print("PDF baixado com sucesso!")
else:
    print("Não foi possível baixar o PDF. Status code:", resposta.status_code)