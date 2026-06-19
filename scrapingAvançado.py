from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import csv
import os


ARQUIVO_SAIDA = "mangas_detalhes.csv"
ESPERA_PADRAO = 10 

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, ESPERA_PADRAO)


def clicar_seguro(elemento):



    for seletor_fechar in [
        "//button[contains(@class,'cookie') and (contains(text(),'Aceitar') or contains(text(),'Fechar') or contains(text(),'OK'))]",
        "//div[contains(@class,'lgpd') or contains(@class,'cookie')]//button",
        "//button[@id='onetrust-accept-btn-handler']",
    ]:
        try:
            driver.find_element(By.XPATH, seletor_fechar).click()
            sleep(0.5)
        except Exception:
            pass

    try:
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elemento)
        sleep(0.5)
        elemento.click()
        return
    except Exception:
        pass

    try:
        driver.execute_script("arguments[0].click();", elemento)
        return
    except Exception:
        pass

    ActionChains(driver).move_to_element(elemento).click().perform()


def texto_seguro(xpath, base=None):
    try:
        contexto = base if base else driver
        return contexto.find_element(By.XPATH, xpath).text.strip()
    except NoSuchElementException:
        return ""


def atributo_seguro(xpath, atributo, base=None):
    try:
        contexto = base if base else driver
        return contexto.find_element(By.XPATH, xpath).get_attribute(atributo).strip()
    except NoSuchElementException:
        return ""


def coletar_detalhe_campo(label):
    try:
        valor = driver.find_element(
            By.XPATH,
            f"//th[normalize-space(.)='{label}']/following-sibling::td"
        ).text.strip()
        if valor:
            return valor
    except NoSuchElementException:
        pass

    try:
        valor = driver.find_element(
            By.XPATH,
            f"//*[contains(@class,'detalhe') or contains(@class,'info') or contains(@class,'especificacao')]"
            f"//*[normalize-space(.)='{label}']/following-sibling::*"
        ).text.strip()
        if valor:
            return valor
    except NoSuchElementException:
        pass

    try:
        valor = driver.find_element(
            By.XPATH,
            f"//*[normalize-space(text())='{label}:']/following-sibling::*[1]"
        ).text.strip()
        if valor:
            return valor
    except NoSuchElementException:
        pass

    return ""


def coletar_dados_manga():

    sleep(2)

    capa = atributo_seguro(
        "//div[contains(@class,'foto') or contains(@class,'imagem') or contains(@class,'capa')]//img[1]",
        "src"
    )
    if not capa:
        capa = atributo_seguro("//div[@id='divFoto']//img | //img[@id='imgProduto']", "src")

    titulo = texto_seguro("//h1") or texto_seguro("//h2[contains(@class,'titulo')]")

    resumo = texto_seguro(
        "//div[contains(@class,'descricao') or contains(@class,'sinopse') "
        "or contains(@id,'descricao') or contains(@id,'sinopse')]"
    )

    autor      = coletar_detalhe_campo("Autor")
    isbn       = coletar_detalhe_campo("ISBN")
    editora    = coletar_detalhe_campo("Editora")
    demografia = coletar_detalhe_campo("Demografia")

    lancamento = (
        coletar_detalhe_campo("Lançamento")
        or coletar_detalhe_campo("Data de Lançamento")
        or coletar_detalhe_campo("Publicação")
    )

    url = driver.current_url

    return {
        "URL":        url,
        "Título":     titulo,
        "Capa":       capa,
        "Resumo":     resumo,
        "Autor":      autor,
        "ISBN":       isbn,
        "Editora":    editora,
        "Demografia": demografia,
        "Lançamento": lancamento,
    }



driver.get("https://mundosinfinitos.com.br/")
sleep(5)

nome_manga = input("Digite o nome do mangá para busca: ").strip()

barra_pesquisa = wait.until(EC.presence_of_element_located((By.ID, "search_txt")))
barra_pesquisa.click()
barra_pesquisa.send_keys(nome_manga)
barra_pesquisa.send_keys(Keys.ENTER)
sleep(5)

resultados = driver.find_elements(
    By.XPATH,
    "//div[contains(@class,'area-infos')]//div[contains(@class,'descricao')]//h4/a"
)

link_colecao = None
for item in resultados:
    if item.text.strip().lower() == nome_manga.lower():
        link_colecao = item.get_attribute("href")
        break


if not link_colecao and resultados:
    print(f"Nenhuma correspondência exata. Usando o primeiro resultado: '{resultados[0].text}'")
    link_colecao = resultados[0].get_attribute("href")

if not link_colecao:
    print("Nenhum mangá encontrado. Encerrando.")
    driver.quit()
    exit()

driver.get(link_colecao)
sleep(4)

try:
    btn_todas = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[contains(text(),'Todas as edições') or contains(text(),'Todas as Edições')]")
    ))
    clicar_seguro(btn_todas)
    sleep(3)
except TimeoutException:
    print("Botão 'Todas as edições' não encontrado — continuando na página atual.")

try:
    btn_ordenar = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[contains(text(),'Ordenar') or contains(text(),'ordenar')]")
    ))
    clicar_seguro(btn_ordenar)
    sleep(1)

    opcao_crescente = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//*[contains(text(),'Edição Crescente') or contains(text(),'edi') and contains(text(),'rescente')]")
    ))
    clicar_seguro(opcao_crescente)
    sleep(3)
except TimeoutException:
    print("Filtro de ordenação não encontrado — prosseguindo sem ordenar.")

links_edicoes = []

while True:
    cards = driver.find_elements(
        By.XPATH,
        "//div[contains(@class,'area-infos')]//h4/a | //div[contains(@class,'item')]//h4/a"
    )
    for card in cards:
        href = card.get_attribute("href")
        if href and href not in links_edicoes:
            links_edicoes.append(href)

    try:
        prox = driver.find_element(
            By.XPATH,
            "//a[contains(@class,'proxima') or contains(text(),'Próxima') or contains(text(),'>')]"
        )
        clicar_seguro(prox)
        sleep(3)
    except NoSuchElementException:
        break  # Sem próxima página → encerra loop

print(f"\n{len(links_edicoes)} edições encontradas. Iniciando coleta de detalhes...\n")

campos = ["URL", "Título", "Capa", "Resumo", "Autor", "ISBN", "Editora", "Demografia", "Lançamento"]
arquivo_existe = os.path.isfile(ARQUIVO_SAIDA)

with open(ARQUIVO_SAIDA, "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=campos)
    if not arquivo_existe:
        writer.writeheader()

    for i, url in enumerate(links_edicoes, 1):
        print(f"[{i}/{len(links_edicoes)}] Coletando: {url}")
        try:
            driver.get(url)
            dados = coletar_dados_manga()
            writer.writerow(dados)
            print(f"  ✔ {dados['Título']}")
        except Exception as e:
            print(f"  ✘ Erro ao coletar {url}: {e}")

print(f"\nColeta concluída! Dados salvos em '{ARQUIVO_SAIDA}'.")
driver.quit()