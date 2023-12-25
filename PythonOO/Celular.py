import docbr as dbr

class CellPhone:
    def __init__(self, cell_phone):
        if self.validation(cell_phone):
            self.cell_phone = cell_phone
        else:
            raise ValueError("Celular Inválido!!")

    def __str__(self):
        return self.format()

    def validation(self, cell_phone):
        cell_phone = dbr.validate(cell_phone, doctype='tfone', lazy=False)
        return cell_phone

    def format(self):
       self.cell_phone = dbr.parse(self.cell_phone, doctype='tfone', mask=True)
       return self.cell_phone
