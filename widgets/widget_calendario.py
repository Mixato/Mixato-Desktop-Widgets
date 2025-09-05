import calendar, datetime, time
#Función para calendario
def calendario_alineado(anno, mes, Marcar_Dia, Dia_Izquierda, Dia_Derecha):
    calendar.setfirstweekday(6)
    cal = calendar.month(anno, mes)
    lineas = cal.splitlines()
    if Marcar_Dia:
         for i in range(len(lineas)):
             if(i != 0) and (i != 1) and (str(mes) == time.strftime("%m").lstrip("0")):
                 Dia_Resaltado = time.strftime("%e")
                 lineas[i] = lineas[i].replace(f" {Dia_Resaltado} ",f"{Dia_Izquierda}{Dia_Resaltado}{Dia_Derecha}")
    lineas[-1] = lineas[-1].ljust(len(lineas[1]))  # Justificar a la izquierda la ultima semana
    return "\n".join(lineas)

def calendario_vertical(anno1, mes_inicial, Marcar_Dia, Dia_Izquierda, Dia_Derecha):

  # Obtener los calendarios de los dos meses
  cal2 = calendario_alineado(anno1, mes_inicial, Marcar_Dia, Dia_Izquierda, Dia_Derecha)
  if (mes_inicial == 12):
      cal3 = calendario_alineado(anno1 + 1, 1, Marcar_Dia, Dia_Izquierda, Dia_Derecha)
  else:   
      cal3 = calendario_alineado(anno1, mes_inicial + 1, Marcar_Dia, Dia_Izquierda, Dia_Derecha)

  # Unir los calendarios en una sola cadena
  calendario_completo = f"{cal2}\n\n{cal3}"

  return calendario_completo

def calendario_semana(anno, mes, ahora, Marcar_Dia, Dia_Izquierda, Dia_Derecha):
    calendar.setfirstweekday(6)
    cal = calendar.month(anno, mes)
    lineas = cal.splitlines()
    ultima_semana = lineas[-1]  
    ultima_semana = ultima_semana.ljust(len(lineas[1]))  # Justificar a la izquierda
    lineas[-1] = ultima_semana
    fecha2 = str(str(anno) +"-" + str(mes) + "-1")
    fecha2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()
    dia = fecha2.isocalendar()[2]
    sem = fecha2.isocalendar()[1]
    if dia == 7:
        sem = sem + 1
    if mes == 12:
        if (dia == 1) or (dia == 7):
            nosem53 = True
    for i in range(len(lineas)):
        if (sem == 53) and (nosem53):
            sem = 1
        if(i != 0):
            if i == 1:
                lineas[i] = f"  W  {lineas[i]}"
            else:
                if sem < 10:
                    if sem != ahora:
                        lineas[i] = f"  {sem}  {lineas[i]}"
                    else:
                        lineas[i] = f" {Dia_Izquierda}{sem}{Dia_Derecha} {lineas[i]}"
                        if Marcar_Dia:
                            Dia_Resaltado = time.strftime("%e")
                            lineas[i] = lineas[i].replace(f" {Dia_Resaltado} ",f"{Dia_Izquierda}{Dia_Resaltado}{Dia_Derecha}")
                    sem = sem + 1
                else:
                    if sem != ahora:
                        lineas[i] = f" {sem}  {lineas[i]}"
                    else:
                        lineas[i] = f"{Dia_Izquierda}{sem}{Dia_Derecha} {lineas[i]}"
                        if Marcar_Dia:
                            Dia_Resaltado = time.strftime("%e")
                            lineas[i] = lineas[i].replace(f" {Dia_Resaltado} ",f"{Dia_Izquierda}{Dia_Resaltado}{Dia_Derecha}")
                    sem = sem + 1
    return "\n".join(lineas)

def calendario_vertical_semana(anno1, mes_inicial, ahora, Marcar_Dia, Dia_Izquierda, Dia_Derecha):

  # Obtener los calendarios de los dos meses
  cal2 = calendario_semana(anno1, mes_inicial, ahora, Marcar_Dia, Dia_Izquierda, Dia_Derecha)
  if (mes_inicial == 12):
      cal3 = calendario_semana(anno1 + 1, 1, ahora, Marcar_Dia, Dia_Izquierda, Dia_Derecha)
  else:   
      cal3 = calendario_semana(anno1, mes_inicial + 1, ahora, Marcar_Dia, Dia_Izquierda, Dia_Derecha)

  # Unir los calendarios en una sola cadena
  calendario_completo = f"{cal2}\n\n{cal3}"

  return calendario_completo