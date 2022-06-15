# Robô de avaliação de investimentos
> Status: Em andamento...

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto](#Sobre)
   * [Pré Requisitos](#pre-requisitos)
   * [Como ler esse projeto?](#como-ler)

<!--te-->



### Sobre o projeto:
[#Sobre]
Este projeto tem como objetivo ler uma página web que contenha uma carteira financeira com moedas e ações e suas respectivas quantidades e levar essas informações para uma planilha excel.
A planilha conterá cada ativo, sua quantidade e o valor total que o proprietário da carteira possui em reais. Além disso, a planilha conterá gráficos referentes ao histórico de cotação de alguns ativos e um Qrcode com o valor total que o proprietário possui em reais na carteira disponibilizada.

### Pré Requisitos:
[#pre-requisitos]
1. Fornecer uma URL que contenha uma tabela apenas com as moedas dentro da tag :
```
<div class='acao'> 
```
e que contenha oura tabela só com as moedas dentro da classe:
```
<div class='moeda'> 
```
2. Os nomes das ações devem estar de acordo com seus nomes no [YahooFinance](https://finance.yahoo.com/)
⚠️ Atenção: Ativos escritos incorretamente não serão tratados  contabilizados

### Como ler esse projeto?
[#como-ler]
Para entender e executar esse projeto siga as seguintes instruções:
-[] Instale em seu computador a biblioteca BeautifulSoup do Python
```
pip install beautifulsoup4
```
-[] Instale a biblioteca Openpyxl do Python
```
<div class='moeda'> 
```
-[] Instale a biblioteca Yfinance do Python
```
<div class='moeda'> 
```
-[] Instale a biblioteca qrcode do Python
```
<div class='moeda'> 
```
-[] Instale os módulos principal.py, excel.py,webscraping.py,financas.py
-[] Coloque todos os módulos na mesma pasta de seu computador
-[] Execute o módulo principal.py
-[] insira uma URL que atenda aos pré-requisitos,caso não tenha uma, utilize nossas carteiras teste:
*[Carteira 1](https://laviniasd.github.io/Robo-de-Avaliacao-de-Investimentos/index.html)
*[Carteira 2](https://laviniasd.github.io/Robo-de-Avaliacao-de-Investimentos/site2/pagina2.html)
*[Carteira 3](https://laviniasd.github.io/Robo-de-Avaliacao-de-Investimentos/site3/pagina3.html)
