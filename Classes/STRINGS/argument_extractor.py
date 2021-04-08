class Argument_Extractor_Url:
    def __init__(self, url):
        if self.valid_url(url):
            self.url = url.lower()
        else:
            raise LookupError("Invalid Url!") 

    def __len__(self):
        return len(self.url)

    def __str__(self):
        currency_origin, currency_target = self.extractor_arguments()
        return f"Value: {self.extract_value()}, from {currency_origin} to {currency_target}."

    def __eq__(self, to_comparer):
        return self.url == to_comparer.url

    @staticmethod
    def valid_url(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False


    def extractor_arguments(self): 
        take_currency_origin = "currencyOrigin".lower()
        take_currency_target = "currencyTarget".lower()

        initial_index_currency_origin = self.find_initial_index(take_currency_origin)
        final_index_currency_origin = self.url.find("&")
        initial_index_currency_target = self.find_initial_index(take_currency_target)
        final_index_currency_target = self.url.find("&valor")
        '''        
        initial_index_currency_target = self.url.find("=",60)+1
        initial_index_currency_origin = self.url.find("=",40)+1
        final_index_currency_origin = self.url.find("&",40)
        '''
        currency_origin = self.url[initial_index_currency_origin : final_index_currency_origin]
        currency_target = self.url[initial_index_currency_target : final_index_currency_target]
        return currency_origin, currency_target

    def find_initial_index(self, search_currency):
        return self.url.find(search_currency) + len(search_currency) + 1

    def extract_value(self):
        value_to_get = "valor"
        initial_index_value = self.find_initial_index(value_to_get)
        value = self.url[initial_index_value: ]
        return value



# www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar

