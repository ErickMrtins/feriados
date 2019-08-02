import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import numpy as np

'''
    Lista com os nomes das cidades que deseja recuperar os feriados.
'''

cidades = ['curitiba-pr', 'colombo-pr', 'londrina-pr', 'americana-sp', 'piracicaba-sp',
           'guarulhos-sp', 'campinas-sp', 'sao_jose-sc', 'balneario_camboriu-sc']

#Captura o ano atual!
ano = datetime.now().year - 10

#abre arquivo csv no modo Escrita
file = open("feriados.csv", "w")

#Busca os feriados por Ano
while ano < 2025:
    ano += 1
    for c in cidades:
        endereco = "http://www.feriados.com.br/feriados-" + c + ".php?ano=" + str(ano)
        header = {
            "User-Agent": "User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

        r = requests.get(endereco, headers=header)

        hmtl = r.content

        res = BeautifulSoup(hmtl, 'html.parser')

        tag = 'span'
        parametro = 'class'
        valorParametro = 'style_lista_feriados'
        valorParametroFacultativo = 'style_lista_facultativos'

        tags = res.findAll(tag, {parametro: valorParametro})


        for f in tags:
            f = f.getText().strip()
            nomeFeriado = f[f.find('-'):]
            nomeFeriado = nomeFeriado.replace("-", "")
            f = f[:f.find('-')]
            feriado = (f + ", " + nomeFeriado + ", " + c)
            print(f + ", " + c + ", " + nomeFeriado)
            escrita = file.write(feriado + "\n")


        tagFacultativos = res.findAll(tag, {parametro: valorParametroFacultativo})

        for fac in tagFacultativos:
            fac = fac.getText().strip()
            nomeFeriado = fac[fac.find('-'):]
            nomeFeriado = nomeFeriado.replace("-", "").strip()
            fac = fac[:fac.find('-')]
            if nomeFeriado == "Carnaval" or nomeFeriado == "Corpus Christi":
                feriadoFacultativo = (fac + ", " + nomeFeriado + ", " + c)
                print(fac + ", " + nomeFeriado + ", " + c)
                escrita = file.write(feriadoFacultativo + "\n")















