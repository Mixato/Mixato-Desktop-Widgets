[Widgets]

#Formato archivo configuración, duplicar éste archivo como config.ini
# Elegir el monitor, se encuentran alineados de izquierda a derecha, siendo el primero de la izquierda el 0
Monitor_Widget = 0
# Usar en caso de querer enviar al monitor de la derecha sin saber la cantidad total de monitores
Full_Derecha = False
# Habilitar que al reiniciar con Click Derecho se cambie el monitor a Full Derecha
Click_Cruce = True
# Usar para colores de fondo oscuros.
Modo_Oscuro = True
# Tiempo de refresco en segundos
Refresh_Seconds = 1

# Habilitar Widget de la hora
Hora = True
Ubicacion_Hora_relx = 0.5
Ubicacion_Hora_rely = 0.02
Ubicacion_Hora_anchor = n
Color_Hora = #d99334
Letra_Hora = Arial Rounded MT Bold
Tamannio_Hora = 60

# Habilitar Widget de la fecha
Fecha = True
Ubicacion_Fecha_relx = 0.5
Ubicacion_Fecha_rely = 0.13
Ubicacion_Fecha_anchor = n
Color_Fecha = #d99334
Letra_Fecha = Roboto
Tamannio_Fecha = 14
Incluir_Semana = True

# Habilitar Widget de mensajes
# La fecha en mensajes del día tiene el formato "aaaa-m-d"
# Los mensajes del día se cargan separando con , y espacio en blanco, deben coincidir la cantidad de fechas con la cantidad de mensajes
# Para Mensaje del día Multilineas escribir \n en donde va el salto de linea
# El mensaje del día aquí cargado solo se mostrará si no existe ningún mensaje del día en messages.txt
Mensajes = True
Ubicacion_Mensajes_relx = 0.02
Ubicacion_Mensajes_rely = 0.02
Ubicacion_Mensajes_anchor = nw
Color_Mensajes = #d99334
Letra_Mensajes = Consolas
Tamannio_Mensajes = 14
Segundo_Mensaje = True
Ubicacion_Mensajes2_relx = 0.98
Ubicacion_Mensajes2_rely = 0.35
Ubicacion_Mensajes2_anchor = ne
Color_Mensajes2 = #d99334
Letra_Mensajes2 = Consolas
Tamannio_Mensajes2 = 14
Color_Mensaje_Dia = red
Mostrar_ayer = True
Mostrar_anteayer = True
Dia_Mensaje = 2024-12-19
Mensaje_Dia = Linea de prueba\nSegunda Linea

# Habilitar Widget del calendario
Calendario = True
Ubicacion_Calendario_relx = 0.98
Ubicacion_Calendario_rely = 0.02
Ubicacion_Calendario_anchor = ne
Color_Calendario = #d99334
Letra_Calendario = Consolas
Tamannio_Calendario = 11
Incluir_Semana_Cal = True
Marcar_Dia = True
Dia_Izquierda = [
Dia_Derecha = ]