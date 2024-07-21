"""AULA 35 --- Datas e Horas"""

# Importa a biblioteca 'datetime' = datas e horas
import datetime

data = datetime.datetime.now() # --- 'now()' = data e hora atual
print(data) # --- 2024-07-21 10:54:42.977359

print(data.second)
print(data.minute)
print(data.hour)
print(data.day)
print(data.weekday())
print(data.month)
print(data.year)

print(f"Hoje é {data.day} de {data.month} de {data.year}.\nAgora é {data.hour}:{data.minute}:{data.second}")

nascimento = datetime.datetime(2004, 5, 18)
print(nascimento) # --- 2004-05-18 00:00:00
print(nascimento.strftime("%A")) # --- Tuesday = terça
# %a = abreviatura do dia da semana
# %A = dia da semana
# %w = dia da semana (0 = domingo, 6 = sabado)
# %d = dia do mês
# %b = abreviatura do nome do mês
# %B = nome do mês
# %m = mês
# %y = ano com dois digitos
# %Y = ano com quatro digitos
# ---
# %H = hora (00-23)
# %I = hora (00-12)
# %p = AM/PM
# %M = minuto
# %S = segundo
# %f = microsegundo
# %z = fusos horários
# %Z = nome do fuso horário (caso não seja informado, o fuso horário é GMT)
# %j = dia do ano (001-366)
# %U = semana do ano (00-53, sendo que a semana começa no domingo)
# %W = semana do ano (00-53, sendo que a semana começa no sábado)

nascimento_preciso = datetime.datetime(year=2004, month=5, day=18, hour=11, minute=45, second=59)
print(nascimento_preciso)

print(nascimento_preciso.strftime("%p"))
print(nascimento_preciso.strftime("%j"))
print(nascimento_preciso.strftime("%w"))
print(nascimento_preciso.strftime("%W"))
print(nascimento_preciso.strftime("%y"))