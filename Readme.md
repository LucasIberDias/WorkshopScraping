# Workshop de Web Scraping com Python e Selenium

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python\&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automação-43B02A?logo=selenium\&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![Licença](https://img.shields.io/badge/Licença-Educacional-blue)

Este repositório contém os materiais utilizados no Workshop de Web Scraping com Python e Selenium.

O objetivo é ensinar desde os conceitos básicos de automação de navegação até técnicas mais avançadas de coleta de dados em sites reais.

---

## Estrutura do Projeto

```text
WorkshopScraping
├── conteudos
│   ├── slides.pptx
│   └── WorkShopResumo.pdf
├── scraping.py
├── scrapingAvancado.py
└── README.md
```

---

## Materiais

### slides.pptx

Apresentação utilizada durante a aula.

### WorkShopResumo.pdf

Material de apoio com resumo dos conceitos abordados no workshop.

---

## Exercício Prático - `scraping.py`

Durante a aula será desenvolvido um scraping simples utilizando Selenium em python, 
para os que não conseguiram acompanhar o arquivo está completo aqui e já comentado.

### Objetivo

Automatizar o processo de:

1. Acessar um site
2. Coletar os nomes dos produtos
3. Coletar os preços dos produtos
4. Percorrer todos os itens da página
5. Salvar os dados em um arquivo CSV

### Site utilizado

https://devaprender-play.netlify.app/

## Ferramentas Utilizadas

<div align="center">

<img width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"/>
<img width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/>

<img width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"/>

</div>

<br>

| Ferramenta | Descrição |
|------------|------------|
| VS Code | Ambiente de desenvolvimento utilizado durante o workshop |
| Python | Linguagem utilizada para desenvolver os crawlers |
| Selenium | Biblioteca responsável pela automação do navegador |
| Git | Controle de versão do projeto |
| CSV | Armazenamento dos dados coletados |
| XPath | Localização e navegação entre elementos HTML |
| Chrome / Chromium | Navegador utilizado durante a automação |

### Resultado esperado

```csv
Produto,Preço
Produto A,R$ 99,90
Produto B,R$ 149,90
Produto C,R$ 59,90
```

---

## Exemplo Avançado - `scrapingAvancado.py`

Este arquivo refere-se a um código de um scraping mais avançdo e robusto, que foi
apresentado após a criação do scraping simples.

### Funcionalidades

* Busca automática de mangás
* Interação com formulários
* Tratamento de exceções
* Paginação automática
* Coleta de dados detalhados
* Exportação para CSV
* Manipulação avançada de elementos
* Uso de funções reutilizáveis

### Dados coletados

* URL
* Título
* Capa
* Resumo
* Autor
* ISBN
* Editora
* Demografia
* Data de lançamento

### Site utilizado

https://mundosinfinitos.com.br/

---

## Instalação

Clone o repositório:

```bash
[git clone https://github.com/seu-usuario/seu-repositorio.git
](https://github.com/LucasIberDias/WorkshopScraping.git)
```

Acesse a pasta:

```bash
cd WorkshopScraping
```

Instale as dependências:

```bash
pip install selenium
```
Em casos de não ser o usuário principal:

```bash
python3 -m venv selenium_env && source selenium_env/bin/activate && pip install --upgrade pip && pip install selenium
```

---

## Executando

### Crawler Básico

```bash
python scraping.py
```

### Crawler Avançado

```bash
python scrapingAvancado.py
```

---

## Conceitos Abordados

* O que é Web Scraping
* Automação de Navegadores
* Selenium WebDriver
* Localização de elementos com XPath
* Coleta de dados
* Manipulação de arquivos
* Boas práticas em crawlers
* Estruturação de projetos de automação

---

## Aviso

Este projeto possui fins exclusivamente educacionais e foi desenvolvido para demonstração durante o workshop de scraping no IFPR - Campus de Cascavel.

Sempre respeite os Termos de Uso, o arquivo `robots.txt` e as políticas dos sites antes de realizar qualquer coleta automatizada de dados.

---

## Autor

Lucas Iber Dias, com fins educacionais.
