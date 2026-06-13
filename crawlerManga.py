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

from selenium import webdriver;
from selenium.webdriver.common.by import By;
import os;
from time import sleep;

driver = webdriver.Chrome('https://mundosinfinitos.com.br/');
driver.get('');
sleep(5);

