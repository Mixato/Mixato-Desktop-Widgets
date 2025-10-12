from tkinter import *
import time, datetime
import locale
from screeninfo import get_monitors
import configparser
import widgets.mixato_widgets as wg
import os, sys, subprocess
locale.setlocale(locale.LC_ALL, "es-ES.UTF-8") # Formato local, Ejemplo Español: locale.setlocale(locale.LC_ALL, "es-ES")

class MixatoWidgetsApp:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(1)
        self.root.bind("<Button-3>", self.Lanzar_Configurador)
        self.root.bind("<Button-2>", self.cerrar)

        # Cargar configuración

        self.Cargar_Configuración()
        self.Configurar_Ventana()
        self.Cargar_Mensaje_Día()

        # Widget Hora
        if (self.Hora):
            self.Texto_Hora = StringVar()
            Label_Hora = Label(self.Frame_Principal, textvariable=self.Texto_Hora, fg=self.Color_Hora, bg=self.transparente, font=(self.Letra_Hora, self.Tamannio_Hora))
            Label_Hora.place(relx=self.Ubicacion_Hora[0], rely=self.Ubicacion_Hora[1], anchor=self.Ubicacion_Hora[2])

        # Widget Fecha
        if (self.Fecha or self.Mensaje_del_Dia):
            self.Texto_Fecha = StringVar()
            Label_Fecha = Label(self.Frame_Principal, textvariable=self.Texto_Fecha, fg=self.Color_Fecha, bg=self.transparente, font=(self.Letra_Fecha, self.Tamannio_Fecha))
            Label_Fecha.place(relx=self.Ubicacion_Fecha[0], rely=self.Ubicacion_Fecha[1], anchor=self.Ubicacion_Fecha[2])
            if (self.Incluir_Semana):
                self.Semana = " [w"+str(self.ahora.isocalendar()[1])+"]"
            if (self.Dia_Separado):
                self.Texto_Fecha.set(value=time.strftime("%e de %B")+self.Semana)
            else:
                self.Texto_Fecha.set(value=time.strftime("%A, %e de %B")+self.Semana)
            if (self.Mensaje_del_Dia):
                self.Texto_Fecha.set(value=self.Mensaje_Dia)
            
        # Widget Mensajes
        if (self.Mensajes):
            self.Texto_Mensaje = StringVar()
            Label_Mensaje = Label(self.Frame_Principal, textvariable=self.Texto_Mensaje, fg=self.Color_Mensajes, bg=self.transparente, font=(self.Letra_Mensajes, self.Tamannio_Mensajes))
            Label_Mensaje.place(relx=self.Ubicacion_Mensajes[0], rely=self.Ubicacion_Mensajes[1], anchor=self.Ubicacion_Mensajes[2])

        if (self.Segundo_Mensaje):
            self.Texto_Mensaje2 = StringVar()
            mensajelabel2 = Label(self.Frame_Principal, textvariable=self.Texto_Mensaje2, fg=self.Color_Mensajes2, bg=self.transparente, font=(self.Letra_Mensajes2, self.Tamannio_Mensajes2))
            mensajelabel2.place(relx=self.Ubicacion_Mensajes2[0], rely=self.Ubicacion_Mensajes2[1], anchor=self.Ubicacion_Mensajes2[2])

        # Widget Calendario
        if (self.Calendario):
            self.Texto_Calendario = StringVar()
            Label_Calendario = Label(self.Frame_Principal, textvariable=self.Texto_Calendario, fg=self.Color_Calendario, bg=self.transparente, font=(self.Letra_Calendario, self.Tamannio_Calendario))
            Label_Calendario.place(relx=self.Ubicacion_Calendario[0], rely=self.Ubicacion_Calendario[1], anchor=self.Ubicacion_Calendario[2])
            if (self.Incluir_Semana_Cal):
                Calendario_Vertical = wg.calendario_semana(self.ahora.year, self.ahora.month, self.ahora.isocalendar()[1], self.Marcar_Dia, self.Dia_Izquierda, self.Dia_Derecha)
            else:
                Calendario_Vertical = wg.calendario_vertical(self.ahora.year, self.ahora.month, self.Marcar_Dia, self.Dia_Izquierda, self.Dia_Derecha)
            if (self.Calendario):
                self.Texto_Calendario.set(value=Calendario_Vertical)
        
        # Widget Día de la semana
        if (self.Dia_Separado):
            dia_con_acento = time.strftime("%A").upper()
            dia_sin_acento = dia_con_acento.replace("É", "E").replace("Á", "A")
            if (self.Letra_Dia_Separado == "Anurati"):
                dia_sin_acento = dia_sin_acento.replace("VI","V I").replace("IE","I E").replace("IN","I N")
            self.Dia_Semana = StringVar()
            self.Dia_Semana.set(value=dia_sin_acento)
            Label_Dia_Semana = Label(self.Frame_Principal, textvariable=self.Dia_Semana, fg=self.Color_Dia_Separado, bg=self.transparente, font=(self.Letra_Dia_Separado, self.Tamannio_Dia_Separado))
            Label_Dia_Semana.place(relx=self.Ubicacion_Dia_Separado[0], rely=self.Ubicacion_Dia_Separado[1], anchor=self.Ubicacion_Dia_Separado[2])


        self.Actualizar_Variables()
            
            
    def Actualizar_Variables(self):
        if (self.Hora):
            self.Texto_Hora.set(value=time.strftime("%H:%M"))
        if (self.Mensajes):
            self.Texto_Mensaje.set(value=wg.print_mensaje(1))
        if (self.Segundo_Mensaje):
            self.Texto_Mensaje2.set(value=wg.print_mensaje(2))
        restart = datetime.datetime.now()       
        if (self.ahora.day != restart.day):
            os.execl(sys.executable, sys.executable, *sys.argv)
        self.Frame_Principal.after(self.RefreshMili, self.Actualizar_Variables)
        self.Aplicar_Config()
        self.Revisar_Cierre()

    def Cargar_Configuración(self):
        # Configuración default
        self.Monitor_Widget = 0 # Se elige el monitor enumerados de izq a der, empezando por 0
        self.Full_Derecha = False # Manda todo a la derecha si tengo 3 monitores
        self.Click_Cruce = False
        self.Modo_Oscuro = False
        self.Solo_Hora = False
        self.Refresh_Seconds = 1
        self.alpha = 1
        self.Hora = True
        self.Ubicacion_Hora = [0.5,0.02,"n"] # Formato: relx=0.98,rely=0.02,anchor="ne" Ejemplo: [0.98,0.02,"ne"]
        self.Letra_Hora = "Consolas"
        self.Tamannio_Hora = 60
        self.Color_Hora = "#FFFFFF"
        self.Fecha = False
        self.Ubicacion_Fecha = [0.5,0.13,"n"] # Formato: relx=0.98,rely=0.11,anchor="ne" Ejemplo: [0.98,0.11,"ne"]
        self.Color_Fecha = "white"
        self.Letra_Fecha = "Consolas"
        self.Tamannio_Fecha = 14
        self.Incluir_Semana = True
        self.Mensajes = False
        self.Ubicacion_Mensajes = [0.02,0.02,"nw"] # Formato: relx=0.98,rely=0.11,anchor="ne" Ejemplo: [0.98,0.11,"ne"]
        self.Color_Mensajes = "white"
        self.Letra_Mensajes = "Consolas"
        self.Tamannio_Mensajes = 14
        self.Segundo_Mensaje = False
        self.Ubicacion_Mensajes2 = [0.98,0.35,"ne"] # Formato: relx=0.98,rely=0.11,anchor="ne" Ejemplo: [0.98,0.11,"ne"]
        self.Color_Mensajes2 = "white"
        self.Letra_Mensajes2 = "Consolas"
        self.Tamannio_Mensajes2 = 14
        self.Calendario = False
        self.Ubicacion_Calendario = [0.98,0.02,"ne"] # Formato: relx=0.98,rely=0.11,anchor="ne" Ejemplo: [0.98,0.11,"ne"]
        self.Color_Calendario = "white"
        self.Letra_Calendario = "Consolas"
        self.Tamannio_Calendario = 11
        self.Color_Mensaje_Dia = "red"
        self.ahora = datetime.datetime.now()
        self.ayer=self.ahora + datetime.timedelta(days=-1)
        self.Mostrar_ayer = True
        self.anteayer=self.ahora + datetime.timedelta(days=-2)
        self.Mostrar_anteayer = True
        self.Incluir_Semana_Cal = False
        self.Marcar_Dia = True
        self.Dia_Izquierda = "*"
        self.Dia_Derecha = "*"
        self.Semana = ""
        self.Dia_Mensaje = ""
        self.Mensaje_Dia = ""
        self.Mensaje_del_Dia = False
        self.lista_dias = []
        self.lista_mensajes = []
        self.Cruce_Monitor = False
        self.Dia_Separado = False
        self.Ubicacion_Dia_Separado = [0.5,0.02,"n"] # Formato: relx=0.98,rely=0.02,anchor="ne" Ejemplo: [0.98,0.02,"ne"]
        self.Letra_Dia_Separado = "Anurati"
        self.Tamannio_Dia_Separado = 60
        self.Color_Dia_Separado = "#FFFFFF"

        # Levanto configuración de config.ini
        # Anulo el color #000001 por cuestiones de funcionamiento, ya que no mostrará diferencias perceptibles con el #000000
        try:
            config = configparser.ConfigParser()
            config.read(["config.ini", "messages.txt"], encoding='utf-8')
        except Exception:
            pass
        try:
            self.Monitor_Widget = config.getint("Widgets","Monitor_Widget")
        except Exception:
            pass
        try:
            self.Full_Derecha = config.getboolean("Widgets","Full_Derecha")
        except Exception:
            pass
        try:
            self.Modo_Oscuro = config.getboolean("Widgets","Modo_Oscuro")
        except Exception:
            pass
        try:
            self.Solo_Hora = config.getboolean("Widgets","Solo_Hora")
        except Exception:
            pass
        try:
            self.Refresh_Seconds = config.getint("Widgets","Refresh_Seconds")
        except Exception:
            pass
        try:
            self.Hora = config.getboolean("Widgets","Hora")
        except Exception:
            pass
        try:
            self.Ubicacion_Hora =  [config.getfloat("Widgets","Ubicacion_Hora_relx"),config.getfloat("Widgets","Ubicacion_Hora_rely"),config.get("Widgets","Ubicacion_Hora_anchor")]
        except Exception:
            pass
        try:
            self.Color_Hora = config.get("Widgets","Color_Hora")
            if self.Color_Hora == "#000001":
                self.Color_Hora = "#000000"
        except Exception:
            pass
        try:
            self.Letra_Hora = config.get("Widgets","Letra_Hora")
        except Exception:
            pass
        try:
            self.Tamannio_Hora = config.getint("Widgets","Tamannio_Hora")
        except Exception:
            pass
        try:
            self.Fecha =  config.getboolean("Widgets","Fecha")
        except Exception:
            pass
        try:
            self.Ubicacion_Fecha =  [config.getfloat("Widgets","Ubicacion_Fecha_relx"),config.getfloat("Widgets","Ubicacion_Fecha_rely"),config.get("Widgets","Ubicacion_Fecha_anchor")]
        except Exception:
            pass
        try:
            self.Color_Fecha = config.get("Widgets","Color_Fecha")
            if self.Color_Fecha == "#000001":
                self.Color_Fecha = "#000000"
        except Exception:
            pass
        try:
            self.Letra_Fecha = config.get("Widgets","Letra_Fecha")
        except Exception:
            pass
        try:
            self.Tamannio_Fecha = config.getint("Widgets","Tamannio_Fecha")
        except Exception:
            pass
        try:
            self.Incluir_Semana = config.getboolean("Widgets","Incluir_Semana")
        except Exception:
            pass
        try:
            self.Mensajes = config.getboolean("Widgets","Mensajes")
        except Exception:
            pass
        try:    
            self.Ubicacion_Mensajes =  [config.getfloat("Widgets","Ubicacion_Mensajes_relx"),config.getfloat("Widgets","Ubicacion_Mensajes_rely"),config.get("Widgets","Ubicacion_Mensajes_anchor")]
        except Exception:
            pass
        try:
            self.Color_Mensajes = config.get("Widgets","Color_Mensajes")
            if self.Color_Mensajes == "#000001":
                self.Color_Mensajes = "#000000"
        except Exception:
            pass
        try:
            self.Letra_Mensajes = config.get("Widgets","Letra_Mensajes")
        except Exception:
            pass
        try:
            self.Tamannio_Mensajes = config.getint("Widgets","Tamannio_Mensajes")
        except Exception:
            pass
        try:
            self.Segundo_Mensaje = config.getboolean("Widgets","Segundo_Mensaje")
        except Exception:
            pass
        try:
            self.Ubicacion_Mensajes2 =  [config.getfloat("Widgets","Ubicacion_Mensajes2_relx"),config.getfloat("Widgets","Ubicacion_Mensajes2_rely"),config.get("Widgets","Ubicacion_Mensajes2_anchor")]
        except Exception:
            pass
        try:
            self.Color_Mensajes2 = config.get("Widgets","Color_Mensajes2")
            if self.Color_Mensajes2 == "#000001":
                self.Color_Mensajes2 = "#000000"
        except Exception:
            pass
        try:
            self.Letra_Mensajes2 = config.get("Widgets","Letra_Mensajes2")
        except Exception:
            pass
        try:
            self.Tamannio_Mensajes2 = config.getint("Widgets","Tamannio_Mensajes2")
        except Exception:
            pass
        try:
            self.Calendario = config.getboolean("Widgets","Calendario")
        except Exception:
            pass
        try:
            self.Ubicacion_Calendario =  [config.getfloat("Widgets","Ubicacion_Calendario_relx"),config.getfloat("Widgets","Ubicacion_Calendario_rely"),config.get("Widgets","Ubicacion_Calendario_anchor")]
        except Exception:
            pass
        try:
            self.Color_Calendario = config.get("Widgets","Color_Calendario")
            if self.Color_Calendario == "#000001":
                self.Color_Calendario = "#000000"
        except Exception:
            pass
        try:    
            self.Letra_Calendario = config.get("Widgets","Letra_Calendario")
        except Exception:
            pass
        try:
            self.Tamannio_Calendario = config.getint("Widgets","Tamannio_Calendario")
        except Exception:
            pass
        try:
            self.Incluir_Semana_Cal = config.getboolean("Widgets","Incluir_Semana_Cal")
        except Exception:
            pass
        try:
            self.Color_Mensaje_Dia = config.get("Widgets","Color_Mensaje_Dia")
            if self.Color_Mensaje_Dia == "#000001":
                self.Color_Mensaje_Dia = "#000000"
        except Exception:
            pass
        try:
            self.Dia_Mensaje = config.get("Widgets","Dia_Mensaje")
        except Exception:
            pass
        try:
            self.Mensaje_Dia = config.get("Widgets","Mensaje_Dia")
        except Exception:
            pass
        try:
            self.Mostrar_ayer = config.getboolean("Widgets","Mostrar_ayer")
        except Exception:
            pass
        try:
            self.Mostrar_anteayer = config.getboolean("Widgets","Mostrar_anteayer")
        except Exception:
            pass
        try:
            self.Click_Cruce = config.getboolean("Widgets","Click_Cruce")
        except Exception:
            pass
        try:
            self.Marcar_Dia = config.getboolean("Widgets","Marcar_Dia")
        except Exception:
            pass
        try:
            self.Dia_Derecha = config.get("Widgets","Dia_Derecha")
        except Exception:
            pass
        try:
            self.Dia_Izquierda = config.get("Widgets","Dia_Izquierda")
        except Exception:
            pass
        try:
            self.Dia_Separado = config.get("Widgets","Dia_Separado")
        except Exception:
            pass
        try:
            self.Ubicacion_Dia_Separado =  [config.getfloat("Widgets","Ubicacion_Dia_Separado_relx"),config.getfloat("Widgets","Ubicacion_Dia_Separado_rely"),config.get("Widgets","Ubicacion_Dia_Separado_anchor")]
        except Exception:
            pass
        try:
            self.Color_Dia_Separado = config.get("Widgets","Color_Dia_Separado")
            if self.Color_Dia_Separado == "#000001":
                self.Color_Dia_Separado = "#000000"
        except Exception:
            pass
        try:
            self.Letra_Dia_Separado = config.get("Widgets","Letra_Dia_Separado")
        except Exception:
            pass
        try:
            self.Tamannio_Dia_Separado = config.getint("Widgets","Tamannio_Dia_Separado")
        except Exception:
            pass
        try:
            self.alpha = config.get("Widgets","Alpha")
        except Exception:
            pass
        try:
            with open("cruce.set", encoding="utf-8") as Archivo_Cruce:
                for linea in Archivo_Cruce:
                    if linea.startswith('True'):
                        self.Cruce_Monitor = True
        except Exception:
            pass

        #Formateo de variables para widget Mensaje del Día (Soporta mostrar solo los de hoy, hoy + ayer y hoy mas ayer mas anteayer):
        self.ahora_dia = str(str(self.ahora.year)+"-"+str(self.ahora.month)+"-"+str(self.ahora.day))
        self.ayer_dia = str(str(self.ayer.year)+"-"+str(self.ayer.month)+"-"+str(self.ayer.day))
        self.anteayer_dia = str(str(self.anteayer.year)+"-"+str(self.anteayer.month)+"-"+str(self.anteayer.day))
        if self.Mostrar_anteayer:
            self.Mostrar_ayer = True
        
        if self.Solo_Hora == True:
            self.Calendario = False
            self.Mensajes = False
            self.Segundo_Mensaje = False
        self.RefreshMili = self.Refresh_Seconds*1000

    def Configurar_Ventana(self):
        # Seteo el fondo transparente dependiendo del modo
        if self.Modo_Oscuro:
            self.transparente = "#000001"
        else:
            self.transparente = self.sumar_color_hex(self.Color_Hora)
        self.root.wm_attributes("-transparentcolor", self.transparente) 
        self.root.attributes('-alpha', str(self.alpha))
        # Encuentro los monitores y los ordeno
        monitores = []
        for m in get_monitors():
            monitores.append (m)
        Monitores_Ordenados = sorted (monitores, key=lambda monitorx: monitorx.x)
        # Habilitar el cruce de monitores, entre mas a la izquierda y mas a la derecha.
        if self.Cruce_Monitor:
            if self.Full_Derecha:
                self.Full_Derecha = False
            else:
                self.Full_Derecha = True
        # Enviar al monitor que esté mas a la derecha si está habilitado Full Derecha
        if self.Full_Derecha:
            self.Monitor_Widget = len(Monitores_Ordenados) - 1
        # Ubico la ventana en el Monitor elegido, sumando o restando los píxeles de inicio de dicho Monitor_Widget.
        self.geometria = "+" + str(Monitores_Ordenados[self.Monitor_Widget].x) + "+" + str(Monitores_Ordenados[self.Monitor_Widget].y) 
        self.root.geometry(self.geometria)
        self.geometria = "+" + str((Monitores_Ordenados[self.Monitor_Widget].x)+500) + "+" + str((Monitores_Ordenados[self.Monitor_Widget].y)+100)
        # Creo el frame dentro de la ventana del tamaño del monitor elegido
        self.Frame_Principal = Frame(root, width=Monitores_Ordenados[self.Monitor_Widget].width, height=Monitores_Ordenados[self.Monitor_Widget].height, bg=self.transparente)
        self.Frame_Principal.grid(row=0,column=0)

    def sumar_color_hex(self, color_hex):
        # Función para obtener el color posterior al definido
        color_decimal = int(color_hex[1:], 16)
        if color_decimal == 0xFFFFFF:
            color_decimal = 0xFFFFFE
        else:
            color_decimal += 1
        color_hex_nuevo = hex(color_decimal)[2:].zfill(6)
        color_hex_nuevo = "#" + color_hex_nuevo.upper()
        return color_hex_nuevo

    def cerrar(self, event):
        os._exit(0)
    
    def reiniciar(self, event):
        if self.Click_Cruce:
            if self.Cruce_Monitor:
                with open('cruce.set', 'w') as configfile:
                    configfile.write('False')
            else:
                with open('cruce.set', 'w') as configfile:
                    configfile.write('True')

        os.execl(sys.executable, sys.executable, *sys.argv)
    
    def Lanzar_Configurador(self, event):
        pythonw_path = sys.executable.replace('python.exe', 'pythonw.exe')
        script_path = os.path.abspath('mixatowgconfig.pyw') # Obtiene la ruta absoluta del script .pyw
        subprocess.Popen([pythonw_path, script_path, self.geometria], creationflags=subprocess.CREATE_NO_WINDOW)

    def Cargar_Mensaje_Día(self):
        lista_dias = self.Dia_Mensaje.split(", ")
        lista_mensajes = self.Mensaje_Dia.split(", ")
        for i in range(len(lista_dias)):
            if (self.ahora_dia == lista_dias[i]):
                self.Color_Hora = self.Color_Mensaje_Dia
                self.Color_Fecha = self.Color_Mensaje_Dia
                self.Mensaje_del_Dia = True
                self.Mensaje_Dia = lista_dias[i]+"\n"+lista_mensajes[i]
                self.Mensaje_Dia = self.Mensaje_Dia.replace(r"\n", "\n")
            if (self.ayer_dia == lista_dias[i] and self.Mostrar_ayer):
                self.Color_Hora = self.Color_Mensaje_Dia
                self.Color_Fecha = self.Color_Mensaje_Dia
                self.Mensaje_del_Dia = True
                self.Mensaje_Dia = lista_dias[i]+"\n"+lista_mensajes[i]
                self.Mensaje_Dia = self.Mensaje_Dia.replace(r"\n", "\n")
            if (self.anteayer_dia == lista_dias[i] and self.Mostrar_anteayer):
                self.Color_Hora = self.Color_Mensaje_Dia
                self.Color_Fecha = self.Color_Mensaje_Dia
                self.Mensaje_del_Dia = True
                self.Mensaje_Dia = lista_dias[i]+"\n"+lista_mensajes[i]
                self.Mensaje_Dia = self.Mensaje_Dia.replace(r"\n", "\n")

    def Aplicar_Config(self):
        with open("reload.set", encoding="utf-8") as Archivo_Reload:
            for linea in Archivo_Reload:
                if linea.startswith('False'):
                    return
        with open('reload.set', 'w') as Archivo_Reload:
            Archivo_Reload.write('False')
        os.execl(sys.executable, sys.executable, *sys.argv)
           
    def Revisar_Cierre(self):
        with open('cerrar.txt', encoding='utf-8') as cerrar_txt:
            for linea in cerrar_txt:
                if linea.startswith('False'):
                    return
        with open('cerrar.txt', 'w') as cerrar_txt:
            cerrar_txt.write('False')
        os._exit(0)

if __name__ == "__main__":
    root = Tk()
    app = MixatoWidgetsApp(root)
    root.mainloop()