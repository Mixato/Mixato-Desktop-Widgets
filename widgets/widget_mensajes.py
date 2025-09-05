
# Leo los mensajes
def print_mensaje(numero):
    lineas_validas = []
    if numero == 1:
         try:
             with open("messages.txt", encoding="utf-8") as Archivo_Mensajes:
                 for linea in Archivo_Mensajes:
                      if linea.startswith('##'):
                           break
                      lineas_validas.append(linea[1:].strip())
                 return "\n".join(lineas_validas)
         except Exception:
            return "Buen Día"
    if numero == 2:
         try:
             with open("messages.txt", encoding="utf-8") as Archivo_Mensajes:
                 for linea in Archivo_Mensajes:
                      if linea.startswith('##'):
                           lineas_validas.append(linea[2:].strip())
                 return "\n".join(lineas_validas)
         except Exception:
            return "Buen Día"
