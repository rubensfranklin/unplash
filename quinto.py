import datetime 
import calendar
import holidays

dias_uteis = []

ano = date.today().year
mes = date.today().month
dia_util = 5

feriados = holidays.country_holidays('BR', subdiv='SP')
_, n_dias_no_mes = calendar.monthrange(ano, mes)

for dia in range(1, n_dias_no_mes+1):
    data = datetime.date(ano, mes, dia)
    if data.weekday() < 5 and data not in feriados:
        dias_uteis.append(data)

dia_pgto = dias_uteis[dia_util-1]
dia_pgto = dia_pgto.strftime('%d/%m/%Y')
print(dia_pgto)
