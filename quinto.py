import datetime 
import calendar
import holidays

# lista que vai receber os dia uteis 
dias_uteis = []

#ano dinamico
ano = date.today().year
#mês dinamico
mes = date.today().month
# Coloquei 5 para o quinto dia util
dia_util = 5

# feriados faz parte da Lib chamada holydays a subdiv='SP' é para são paulo
feriados = holidays.country_holidays('BR', subdiv='SP')
# o _ é pra excluir o week day,depois ele pega da lib clanedar todos os dias do mes
_, n_dias_no_mes = calendar.monthrange(ano, mes)

# para cada dia do mes(n_dias_no_mes),
# E usei o 1 para colocar o primeiro dia na posição 1 e +1 para a ultima
for dia in range(1, n_dias_no_mes+1):
    data = datetime.date(ano, mes, dia)
    # Se não for dia da semana E a data nãoestiver na feriados
    if data.weekday() < 5 and data not in feriados:
        #acrescente na lista dia util
        dias_uteis.append(data)
# -1 é pra colocar  o primeiro elemento da lista
dia_pgto = dias_uteis[dia_util-1]
# muda o formato de aaaa-mm-dd para dd-mm-aaaa
dia_pgto = dia_pgto.strftime('%d/%m/%Y')
print(dia_pgto)
