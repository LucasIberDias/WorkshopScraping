# Repita os passos manuais, usando código

# 1° entrar no site = https://devaprender-play.netlify.app/
# 2° Anotar o nome do primeiro produto
# 3° ANotar o preço do primeiro produto
# 4° Repitir para todos os produtos da página
# 5° Guardar informações em arquivo de texto

from selenium import webdriver;
from selenium.webdriver.common.by import By;
import os;
from time import sleep;

driver = webdriver.Chrome();
driver.get('https://devaprender-play.netlify.app/');
sleep(5);

#Para pegar os elementos utilizamos o XPATH(identificador de elementos no site)
#para fazer o XPATH você precisa:
# //[@atributo='valor']

#assim estamos anotando o elemento em uma váriavel, sendo o elemento que for pego pelo XPATH
produtos = driver.find_elements(By.XPATH, "//h3[@class= 'text-lg font-semibold text-gray-900 group-hover:text-indigo-600']");

precos = driver.find_elements(By.XPATH, "//p[@class= 'text-2xl font-bold text-indigo-600']")

for produto, preco in zip(produtos, precos):
    with open('precos.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{produto.text},{preco.text}{os.linesep}');


input('');