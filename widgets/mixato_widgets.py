from . import widget_mensajes
from . import widget_calendario

def print_mensaje(numero):
    return widget_mensajes.print_mensaje(numero)

def calendario_vertical(anno, mes_inicial, Marcar_Dia, Dia_Izquierda, Dia_Derecha):
    return widget_calendario.calendario_vertical(anno, mes_inicial, Marcar_Dia, Dia_Izquierda, Dia_Derecha)

def calendario_semana(anno, mes_inicial, ahora, Marcar_Dia, Dia_Izquierda, Dia_Derecha):
    return widget_calendario.calendario_vertical_semana(anno, mes_inicial, ahora, Marcar_Dia, Dia_Izquierda, Dia_Derecha)