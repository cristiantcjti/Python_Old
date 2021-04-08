from argument_extractor import Argument_Extractor_Url

# www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar

url = 'https://bytebank.com/cambio?currencyOrigin=real&currencyTarget=dolar&valor=1500'

argument1 = Argument_Extractor_Url(url)
currency_origin, currency_target  = argument1.extractor_arguments()
value = argument1.extract_value()


argument2 = Argument_Extractor_Url(url)
currency_origin, currency_target  = argument2.extractor_arguments()
value = argument2.extract_value()

print(argument1)
