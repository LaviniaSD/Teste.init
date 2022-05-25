
from urllib.request import urlopen
from bs4 import BeautifulSoup
import yfinance as yf


html = urlopen("file:///C:/Users/B46842/OneDrive%20-%20Fundacao%20Getulio%20Vargas%20-%20FGV/IC_A2/pagina.html")

bs = BeautifulSoup(html, 'html.parser')
linhas_moeda = bs.find_all('tr', {class ='moeda'})

dicionario = {}

for i in linhas_moeda:
    children = i.findChildren("td")
    dicionario[children[0].text] = int(children[1].text)

print(dicionario)

acumulado = 0
for chave in dicionario.keys():
    tipo = chave
    valor = yf.Ticker(tipo).info.get('currentPrice')#Funciona só para ações  #Verificar se todas as ações estão em dólar
    quantidade = dicionario[chave]
    acumulado += quantidade*valor
    
#print(acumulado)

for chave in dicionario.keys():
    hist = yf.download(tickers=chave, period = '5y')
    chave = yf.Ticker(chave)
    #print(chave.history())
    #print(hist)




valor = yf.Ticker('USD').history()
#print(valor)
print(valor[['Close']])




#No caso de moedas, procurar dentro do dicionario yf.Ticker(tipo).info a chave ['description'], e
#dentro dessa chave o texto The last known price of ... is 'VALOR QUE QUEREMOS'
#Perguntar para o Pinho
        
    
#útil pra pegarmos o histórico 
#valor = yf.download(tickers=tipo, period = '1m')    


moeda ='USD'
print(moeda+'BRL=X')

valor = yf.Ticker('VALE').info #.get('currentPrice')#Funciona só para ações  #Verificar se todas as ações estão em dólar
print(valor)
