# 1 - entrar no site = https://mundosinfinitos.com.br/
# 2 - Abrir barra de pesquisa
# 3 - Colocar nome do mangá
# 4 - Apertar o botão de busca
# 5 - Abre o primeiro mangá que nome == mangá
# 6 - Seleciona Todas as edições
# 7 - Seleciona ordenar
# 8 - Coloca filtro #Edição Crescente
# 9 - Abre primeiro mangá
# 10 - Coleta Capa
# 11 - Coleta Titulo
# 12 - Coleta detalhes do produto = Resumo do capitulo
# 13 - Coleta Autor
# 14 - Coleta ISBN
# 15 - Coleta Editora
# 16 - Coleta Demografia
# 17 - Coleta data-lançamento
# 18 - Retorna
# 19 - Coleta proximo mangá

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# 1 - entrar no site = https://mundosinfinitos.com.br/
# Seleciona o site que vou pegar os dados, e da um tempo de 5 segundos de espera para garantir que não vai tentar pegar dados sem o site ter sido aberto totalmente

driver = webdriver.Chrome()

# Maximiza a janela para a barra de pesquisa ficar visível
driver.maximize_window()

# Abre a URL colocada
driver.get("https://mundosinfinitos.com.br/")
sleep(5)

# 2 - Abrir barra de pesquisa
# 3 - Colocar nome do mangá
# Seleciona a barra de pesquisa e coloca o nome do mangá

nome_manga = input("Digite o nome do mangá para busca: ")
barra_pesquisa = driver.find_element(By.ID, "search_txt")
barra_pesquisa.click()

# Digita o nome e aperta ENTER
barra_pesquisa.send_keys(nome_manga)
barra_pesquisa.send_keys(Keys.ENTER)

sleep(10)