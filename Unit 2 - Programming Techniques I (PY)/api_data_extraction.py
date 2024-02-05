import os
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError
import json
import pandas as pd


def captura_de_erros(url_: str) -> requests.models.Response:
    """
    Realiza a requisição HTTP GET e testa possíveis erros.
    Retorna a resposta da requisição.
    """
    try:
        adaptador = HTTPAdapter(max_retries=5)
        sessao = requests.Session()
        sessao.mount(url, adaptador)
        resposta_ = sessao.get(url_)
    except HTTPError as http_err:
        print(f"Ocorreu um erro HTTP: {http_err}")
        erros.write(url)
    except ConnectionError as ce:
        print(f"Ocorreu um erro de conexão: {ce}")
        erros.write(url)
    except Exception as e:
        print(f"Ocorreu outro tipo de erro: {e}")
        erros.write(url)
    else:
        if resposta_.status_code != 200:
            resposta_ = None
        return resposta_


erros = open(f"{os.path.abspath("datasets")}\\erros.txt", "w")
totais = open(f"{os.path.abspath("datasets")}\\totais.txt", "a")

urls_salic = ["http://api.salic.cultura.gov.br/v1/projetos",
              "http://api.salic.cultura.gov.br/v1/propostas",
              "http://api.salic.cultura.gov.br/v1/incentivadores",
              "http://api.salic.cultura.gov.br/v1/fornecedores",
              "http://api.salic.cultura.gov.br/v1/proponentes",
              ]

print("""OPÇÕES DE EXTRAÇÃO:
[1] Projetos
[2] Propostas
[3] Incentivadores
[4] Fornecedores
[5] Proponentes
[6] De arquivo
""")

opcao = 0
while not opcao:
    try:
        opcao = int(input("Escolha uma das opções acima para extrair: "))
    except ValueError:
        print("Informe apenas números inteiros.\n")
        continue
    if not (1 <= opcao <= 6):
        print("Informe um número inteiro entre 1 a 5 (inclusivos).\n")
        opcao = 0

urls = []
if 1 <= opcao <= 5:
    urls.append(urls_salic[opcao - 1])
else:
    try:
        caminho = input("\nInforme o caminho completo do arquivo: ")
        arquivo = open(caminho, "r")
        urls = arquivo.read().split("\n")
    except FileNotFoundError:
        print("Caminho não encontrado. Encerrando...")

for url in urls:
    entidade = url.split("/")[-1]
    dados = []
    resposta = captura_de_erros(url)

    if resposta is None:
        continue
    elif resposta.status_code == 200:
        total = resposta.json()["total"]
        totais.write(f"{entidade.title()}: {total}\n")
        print(f"\nTotal de {entidade}: {total}")

        for i in range(0, total + 1, 100):
            pagina = f"{url}/?limit=100&offset={i}&"
            resposta = captura_de_erros(pagina)

            if resposta is None:
                continue

            conteudo = resposta.text

            while "\xa0" in conteudo:
                conteudo = conteudo.replace("\xa0", " ")

            conteudo = json.loads(conteudo)
            dados.extend(conteudo["_embedded"][entidade])

            if i % 1000 == 0:
                print(f"Request {i} realizado com sucesso...")
    else:
        erros.write(f"Não foi possível fazer o request de {url}. Status code: ({resposta.status_code})\n")
        continue

    df = pd.DataFrame(dados)
    df.to_excel(f"{os.path.abspath("datasets")}\\{entidade}.xlsx", engine="xlsxwriter", index=False)
    print(f"\nPlanilha excel de {entidade} criada com sucesso.\n\n")

erros.close()
totais.close()
print("Encerrando...")
