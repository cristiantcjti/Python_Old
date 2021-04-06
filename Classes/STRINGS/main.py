from argument_extractor import Argument_Extractor_Url

# www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar

url = 'www.bytebank.com.br/cambio?currencyOrigin=real&currencyTarget=dolar'

argument = Argument_Extractor_Url(url)

currency_origin, currency_target  = argument.extractor()

print(currency_origin, currency_target)
