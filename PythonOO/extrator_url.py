import re

class ExtratorURL:
    def __init__(self,url):
        self.url = self.sanitization(url)
        self.validation()
    def sanitization(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validation(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        standard_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = standard_url.match(self.url)
        if not match:
            raise ValueError("A URL está vazia")

    @property
    def base(self):
        question_index = self.url.find("?")
        base = self.url[:question_index]
        return base

    @property
    def parameters(self):
        question_index = self.url.find("?")
        parameters = self.url[question_index + 1:]
        return parameters

    def search_parameter(self, search_parameter):
        parameter_index = self.parameters.find(search_parameter)
        value_index = parameter_index + len(search_parameter) + 1
        comercial_index = self.parameters.find("&", value_index)
        if comercial_index == -1:
            value = self.parameters[value_index:]
        else:
            value = self.parameters[value_index:comercial_index]
        return value

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "URL: " + self.url + "\n" + "URL BASE: " + self.base + "\n" + "URL PARAMETROS: " + self.parameters

    def __eq__(self, other):
        return  self.url == other.url

url= "http://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
extrator_url = ExtratorURL (url)

valor_quantidade = extrator_url.search_parameter("quantidade")
moeda_destino = extrator_url.search_parameter("moedaDestino").upper()
moeda_origem = extrator_url.search_parameter("moedaOrigem").upper()

VALOR_DOLAR = 5.50
VALOR_QUANTIDADE = int(valor_quantidade)
conversor = VALOR_QUANTIDADE * VALOR_DOLAR

print(f"Você tem {valor_quantidade} {moeda_origem} o que daria {conversor} {moeda_destino} ")

