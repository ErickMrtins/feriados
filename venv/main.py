import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import numpy as np


cidades = ['curitiba-pr', 'colombo-pr', 'londrina-pr', 'americana-sp', 'piracicaba-sp',
           'guarulhos-sp', 'campinas-sp', 'sao_jose-sc', 'balneario_camboriu-sc']


ano = datetime.now().year
file = open("feriados.csv", "w")
while ano < 2020:
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
        valorParametroFAcultativo = 'style_lista_facultativos'


        tag = res.findAll(tag, {parametro: valorParametro})

        #print(c)
        for f in tag:
            f = f.getText().strip()
            f = f.replace("-", ",").strip()
            feriado = (f + ", " + c)
            print(f + ", " + c)
            escrita = file.write(feriado + "\n")















