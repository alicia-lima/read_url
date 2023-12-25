from datetime import datetime, timezone, timedelta
from pytz import timezone

class DataBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format()
    
    def format(self):
        time_zone = timezone('America/Maceio')
        date_local = self.momento_cadastro.astimezone(time_zone)
        momento_cadastro = date_local.strftime('%d/%m/%Y %H:%M')
        return momento_cadastro
    
    def mes_cadastro(self):
        meses_do_ano = [
            "Janeiro", "Fevereiro", "Março","Abril",
             "Maio", "Junho", "Julho", "Agosto",
            "Setembro", "Outrubro", "Novembro", "Dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month -1
        return meses_do_ano [mes_cadastro]

    def dia_semana(self):
        dias_semana = [
            "Segunda", "Terça", "Quarta", "Quinta",
            "Sexta", "Sabado", "Domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]

    def register_time(self):
        register_time = (datetime.today()) - self.momento_cadastro
        return register_time
