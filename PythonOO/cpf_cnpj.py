import docbr as dbr

class Document:

    @staticmethod
    def document_create(document):
        if len(document) == 11:
            return DocCpf(document)
        elif len(document) == 14:
            return DocCnpj (document)
        else:
            raise ValueError ("Documento Inválido!!")

class DocCpf:
    def __init__(self, document):
        if self.validation(document):
            self.cpf = document
        else:
            raise ValueError("CPF Inválido!!")

    def __str__(self):
        return self.format()

    def validation(self, document):
        cpf = dbr.validate(document, doctype='cpf', lazy=False)
        return cpf

    def format(self):
       self.cpf = dbr.parse(self.cpf, doctype='cpf', mask=True)
       return self.cpf

class DocCnpj:
    def __init__(self, document):
        if self.validation(document):
            self.cnpj = document
        else:
            raise ValueError("CNPJ Inválido!!")

    def __str__(self):
        return self.format()

    def validation(self, document):
        cnpj = dbr.validate(document, doctype='cnpj', lazy=False)
        return cnpj

    def format(self):
       self.cnpj = dbr.parse(self.cnpj, doctype='cnpj', mask=True)
       return self.cnpj




