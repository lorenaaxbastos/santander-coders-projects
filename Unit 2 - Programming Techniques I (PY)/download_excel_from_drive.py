from os import path
import gdown

with open(path.abspath("datasets/urls.csv"), "r") as arquivo:
    entidades = []
    urls = []
    for i, linha in enumerate(arquivo):
        if i != 0:
            entidade, url = linha.split(",")
            entidades.append(entidade)
            urls.append(url)

for entidade, url in zip(entidades, urls):
    gdown.download(url, path.abspath(f"datasets/{entidade}.xlsx"), quiet=False, fuzzy=True)