# imports utilizados

import pyautogui as auto
import time
import pandas as pd

# tempo de execução de cada comando do pyautogui
auto.PAUSE = 0.2

# Passo a passo do projeto

# Passo 1: Abrir o navegador

auto.press("win")
auto.write("opera")
auto.press("enter")

# Passo 2: entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login

time.sleep(2)
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
auto.write(site)
auto.press("enter")

# Passo 3: Acessar o site com login e senha

time.sleep(3)
auto.click(x=508, y=404)

auto.write("marcosvinicius@gmail.com")
auto.press("tab")

auto.write("minhasenha")
auto.press("enter")

# Passo 4: Importar a base de dados

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 5: Inserir todas as informações do produto e repetir o processo para cada um dos produtos

for linha in tabela.index:
    time.sleep(0.5)

    auto.click(x=558, y=287)

    codigo = tabela.loc[linha, "codigo"] 
    auto.write(codigo)
    auto.press("tab")

    marca = tabela.loc[linha, "marca"]  
    auto.write(marca)
    auto.press("tab")
    
    tipo = tabela.loc[linha, "tipo"]
    auto.write(tipo)
    auto.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])         
    auto.write(categoria)
    auto.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    auto.write(preco_unitario)
    auto.press("tab")

    custo = str(tabela.loc[linha, "custo"])            
    auto.write(custo)
    auto.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        auto.write(obs)
    auto.press("enter")
    auto.scroll(1000)