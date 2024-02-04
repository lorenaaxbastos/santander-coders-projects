import os
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError
import json
import pandas as pd


def errors_catch(url_):
    try:
        response_ = session.get(url_, timeout=(5, 10))
    except Timeout:
        print("O request teve timeout")
        erros.write(f"O request teve timeout. | {url_}\n")
    except HTTPError as http_err:
        print("Ocorreu um erro HTTP")
        erros.write(f"Ocorreu um erro HTTP: {http_err} | {url_}\n")
    except ConnectionError as ce:
        print("Ocorreu um erro de conexão")
        erros.write(f"Ocorreu um erro de conexão: {ce} | {url_}\n")
    except Exception as e:
        print("Ocorreu outro tipo de erro")
        erros.write(f"Ocorreu outro tipo de erro: {e} | {url_}\n")
    else:
        return response_


api_adapter = HTTPAdapter(max_retries=3)

erros = open(f"{os.path.abspath("datasets")}\\erros.txt", "w")
totais = open(f"{os.path.abspath("datasets")}\\totais.txt", "w")

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

    session = requests.Session()
    session.mount(url, api_adapter)
    response = errors_catch(url)

    if response is None:
        continue
    elif response.status_code == 200:
        total = response.json()["total"]
        totais.write(f"{entidade.title()}: {total}\n")
        print(f"\nTotal de {entidade}: {total}")

        for i in range(0, total + 1, 100):
            pagina = f"{url}/?limit=100&offset={i}&"

            session = requests.Session()
            session.mount(pagina, api_adapter)
            response = errors_catch(pagina)

            if response is None:
                continue

            conteudo = response.text

            while "\xa0" in conteudo:
                conteudo = conteudo.replace("\xa0", " ")

            conteudo = json.loads(conteudo)
            dados.extend(conteudo["_embedded"][entidade])

            if i % 1000 == 0:
                print(f"Request {i} realizado com sucesso...")
    else:
        erros.write(f"Não foi possível fazer o request de {url}. Status code: ({response.status_code})\n")
        continue

    df = pd.DataFrame(dados)
    df.to_excel(f"{os.path.abspath("datasets")}\\{entidade}.xlsx", engine="xlsxwriter", index=False)
    print(f"Planilha excel de {entidade} criada com sucesso.")

erros.close()
totais.close()
print("Encerrando...")
