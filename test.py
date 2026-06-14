from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import re

# 1 - Entrar no site
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mundosinfinitos.com.br/")
sleep(5)

# 2/3 - Abrir barra de pesquisa e digitar o nome do mangá
nome_manga = input("Digite o nome do mangá para busca: ")
barra_pesquisa = driver.find_element(By.ID, "search_txt")
barra_pesquisa.click()
barra_pesquisa.send_keys(nome_manga)
barra_pesquisa.send_keys(Keys.ENTER)
sleep(5)

# Coleta os nomes dos mangás da página
mangasDaPagina = driver.find_elements(By.XPATH, "//div[@class='area-infos']//div[@class='descricao']//h4/a")

# Lista sem repetição mantendo ordem
mangas_unicos = list(dict.fromkeys(m.text.strip() for m in mangasDaPagina if m.text.strip()))

# Remove o número do volume do final do título para extrair só o nome da série
# Padrões removidos do final: "- 01", "Vol. 01", "Vol 01"
padrao_volume = re.compile(r'[\s\-]*(Vol\.?\s*)?\d+\s*$', re.IGNORECASE)

def extrair_serie(titulo):
    # Remove pontuação solta no final após tirar o número (ex: "One Piece -" → "One Piece")
    serie = padrao_volume.sub('', titulo).strip(' -:')
    # Normaliza capitalização: Title Case
    return serie.title()

# Agrupa em séries únicas sem repetição, mantendo ordem de aparição
series_vistas = []
series_set = set()
for manga in mangas_unicos:
    serie = extrair_serie(manga)
    if serie not in series_set:
        series_set.add(serie)
        series_vistas.append(serie)

# Exibe as séries encontradas para o usuário escolher
print(f"\nSéries encontradas para '{nome_manga}':")
for i, serie in enumerate(series_vistas, start=1):
    print(f"  [{i}] {serie}")

# Usuário escolhe a série
while True:
    try:
        escolha = int(input(f"\nDigite o número da série desejada (1 a {len(series_vistas)}): "))
        if 1 <= escolha <= len(series_vistas):
            serie_escolhida = series_vistas[escolha - 1]
            break
        else:
            print(f"Por favor, digite um número entre 1 e {len(series_vistas)}.")
    except ValueError:
        print("Entrada inválida. Digite apenas um número.")

print(f"\nSérie selecionada: {serie_escolhida}")
# A partir daqui você filtra os volumes da série escolhida e faz a coleta