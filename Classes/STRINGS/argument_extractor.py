class Argument_Extractor_Url:
    def __init__(self, url):
        if self.valid_url(url):
            self.url = url
        else:
            raise LookupError("Invalid Url!") 

    @staticmethod
    def valid_url(url):
        if url:
            return True
        else:
            return False

    def extractor(self):
        take_currency_origin = "currencyOrigin"
        take_currency_target = "currencyTarget"

        initial_index_currency_origin = self.find_initial_index(take_currency_origin)
        final_index_currency_origin = self.url.find("&")
        initial_index_currency_target = self.find_initial_index(take_currency_target)

        '''        
        initial_index_currency_target = self.url.find("=",60)+1
        initial_index_currency_origin = self.url.find("=",40)+1
        final_index_currency_origin = self.url.find("&",40)
        '''
        
        currency_origin = self.url[initial_index_currency_origin : final_index_currency_origin]
        currency_target = self.url[initial_index_currency_target : ]
        return currency_origin, currency_target

    def find_initial_index(self, search_currency):
        return self.url.find(search_currency) + len(search_currency) + 1



# www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar

