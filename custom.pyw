import customtkinter
import time, datetime
import locale
import configparser
#locale.setlocale(locale.LC_ALL, "es-ES.UTF-8") # Formato local, Ejemplo Español: locale.setlocale(locale.LC_ALL, "es-ES")

class crear_ventana :

    def __init__(self, root):  
        self.root = root
        self.root.title("Mixato Widgets - Preferencias")
        self.Cargar_Configuración()
        self.Configurar_Ventana()

    def Configurar_Ventana(self):  
        Label_Hora=customtkinter.CTkLabel(self.root, text="Mostrar Hora:")
        Label_Hora.grid(row=1, column=1)
    
    def Cargar_Configuración(self):
        # Configuración default
        self.ConfigDic = {"Monitor_Widget" : 0} # Se elige el monitor enumerados de izq a der, empezando por 0
        self.ConfigDic["Full_Derecha"] = False # Manda todo a la derecha si tengo 3 monitores
        self.ConfigDic["Click_Cruce"] = False
        self.ConfigDic["Modo_Oscuro"] = False
        self.ConfigDic["Refresh_Seconds"] = 1
        self.ConfigDic["Hora"] = True
        self.ConfigDic["Ubicacion_Hora"] = [0.5,0.02,"n"] # Formato: relx=0.98,rely=0.02,anchor="ne" Ejemplo: [0.98,0.02,"ne"]
        self.ConfigDic["Letra_Hora"] = "Consolas"
        self.ConfigDic["Tamannio_Hora"] = 60
        self.ConfigDic["Color_Hora"] = "#FFFFFF"
        self.ConfigDic["Fecha"] = False
        self.ConfigDic["Ubicacion_Fecha"] = [0.5,0.13,"n"] # Formato: relx=0.98,rely=0.11,anchor="ne" Ejemplo: [0.98,0.11,"ne"]
        self.ConfigDic["Color_Fecha"] = "white"
        self.ConfigDic["Letra_Fecha"] = "Consolas"
        self.ConfigDic["Tamannio_Fecha"] = 14
        self.ConfigDic["Incluir_Semana"] = True
        self.ConfigDic["Mensajes"] = False
        self.ConfigDic["Ubicacion_Mensajes"] = [0.02,0.02,"nw"] # Formato: relx=0.98,rely=0.11,anchor="ne" Ejemplo: [0.98,0.11,"ne"]
        self.ConfigDic["Color_Mensajes"] = "white"
        self.ConfigDic["Letra_Mensajes"] = "Consolas"
        self.ConfigDic["Tamannio_Mensajes"] = 14
        self.ConfigDic["Segundo_Mensaje"] = False
        self.ConfigDic["Ubicacion_Mensajes2"] = [0.98,0.35,"ne"] # Formato: relx=0.98,rely=0.11,anchor="ne" Ejemplo: [0.98,0.11,"ne"]
        self.ConfigDic["Color_Mensajes2"] = "white"
        self.ConfigDic["Letra_Mensajes2"] = "Consolas"
        self.ConfigDic["Tamannio_Mensajes2"] = 14
        self.ConfigDic["Calendario"] = False
        self.ConfigDic["Ubicacion_Calendario"] = [0.98,0.02,"ne"] # Formato: relx=0.98,rely=0.11,anchor="ne" Ejemplo: [0.98,0.11,"ne"]
        self.ConfigDic["Color_Calendario"] = "white"
        self.ConfigDic["Letra_Calendario"] = "Consolas"
        self.ConfigDic["Tamannio_Calendario"] = 11
        self.ConfigDic["Color_Mensaje_Dia"] = "red"
        self.ahora = datetime.datetime.now()
        self.ayer=self.ahora + datetime.timedelta(days=-1)
        self.ConfigDic["Mostrar_ayer"] = True
        self.anteayer=self.ahora + datetime.timedelta(days=-2)
        self.ConfigDic["Mostrar_anteayer"] = True
        self.ConfigDic["Incluir_Semana_Cal"] = False
        self.ConfigDic["Marcar_Dia"] = True
        self.ConfigDic["Dia_Izquierda"] = "*"
        self.ConfigDic["Dia_Derecha"] = "*"
        self.ConfigDic["Semana"] = ""
        self.ConfigDic["Dia_Mensaje"] = ""
        self.ConfigDic["Mensaje_Dia"] = ""
        self.ConfigDic["Mensaje_del_Dia"] = False
        self.ConfigDic["lista_dias"] = []
        self.ConfigDic["lista_mensajes"] = []
        self.ConfigDic["Cruce_Monitor"] = False

        # Levanto configuración de config.ini
        # Anulo el color #000001 por cuestiones de funcionamiento, ya que no mostrará diferencias perceptibles con el #000000
        try:
            self.config = configparser.ConfigParser()
            self.config.read(["config.ini"], encoding='utf-8')
        except Exception:
            pass
        #try:
        #    self.config = configparser.ConfigParser()
        #    self.config.read("config.bak", encoding='utf-8')
        #except Exception:
        #    pass
        try:
            self.ConfigDic["Monitor_Widget"] = self.config.getint("Widgets","Monitor_Widget")
        except Exception:
            pass
        try:
            self.ConfigDic["Full_Derecha"] = self.config.getboolean("Widgets","Full_Derecha")
        except Exception:
            pass
        try:
            self.ConfigDic["Modo_Oscuro"] = self.config.getboolean("Widgets","Modo_Oscuro")
        except Exception:
            pass
        try:
            self.ConfigDic["Refresh_Seconds"] = self.config.getint("Widgets","Refresh_Seconds")
        except Exception:
            pass
        try:
            self.ConfigDic["Hora"] = self.self.config.getboolean("Widgets","Hora")
        except Exception:
            pass
        try:
            self.ConfigDic["Ubicacion_Hora"] =  [self.config.getfloat("Widgets","Ubicacion_Hora_relx"),self.config.getfloat("Widgets","Ubicacion_Hora_rely"),self.config.get("Widgets","Ubicacion_Hora_anchor")]
        except Exception:
            pass
        try:
            self.ConfigDic["Color_Hora"] = self.config.get("Widgets","Color_Hora")
            if self.ConfigDic["Color_Hora"] == "#000001":
                self.ConfigDic["Color_Hora"] = "#000000"
        except Exception:
            pass
        try:
            self.ConfigDic["Letra_Hora"] = self.config.get("Widgets","Letra_Hora")
        except Exception:
            pass
        try:
            self.ConfigDic["Tamannio_Hora"] = self.config.getint("Widgets","Tamannio_Hora")
        except Exception:
            pass
        try:
            self.ConfigDic["Fecha"] = self.config.getboolean("Widgets","Fecha")
        except Exception:
            pass
        try:
            self.ConfigDic["Ubicacion_Fecha"] =  [self.config.getfloat("Widgets","Ubicacion_Fecha_relx"),self.config.getfloat("Widgets","Ubicacion_Fecha_rely"),self.config.get("Widgets","Ubicacion_Fecha_anchor")]
        except Exception:
            pass
        try:
            self.ConfigDic["Color_Fecha"] = self.config.get("Widgets","Color_Fecha")
            if self.ConfigDic["Color_Fecha"] == "#000001":
                self.ConfigDic["Color_Fecha"] = "#000000"
        except Exception:
            pass
        try:
            self.ConfigDic["Letra_Fecha"] = self.config.get("Widgets","Letra_Fecha")
        except Exception:
            pass
        try:
            self.ConfigDic["Tamannio_Fecha"] = self.config.getint("Widgets","Tamannio_Fecha")
        except Exception:
            pass
        try:
            self.ConfigDic["Incluir_Semana"] = self.config.getboolean("Widgets","Incluir_Semana")
        except Exception:
            pass
        try:
            self.ConfigDic["Mensajes"] = self.config.getboolean("Widgets","Mensajes")
        except Exception:
            pass
        try:    
            self.ConfigDic["Ubicacion_Mensajes"] = [self.config.getfloat("Widgets","Ubicacion_Mensajes_relx"),self.config.getfloat("Widgets","Ubicacion_Mensajes_rely"),self.config.get("Widgets","Ubicacion_Mensajes_anchor")]
        except Exception:
            pass
        try:
            self.ConfigDic["Color_Mensajes"] = self.config.get("Widgets","Color_Mensajes")
            if self.ConfigDic["Color_Mensajes"] == "#000001":
                self.ConfigDic["Color_Mensajes"] = "#000000"
        except Exception:
            pass
        try:
            self.ConfigDic["Letra_Mensajes"] = self.config.get("Widgets","Letra_Mensajes")
        except Exception:
            pass
        try:
            self.ConfigDic["Tamannio_Mensajes"] = self.config.getint("Widgets","Tamannio_Mensajes")
        except Exception:
            pass
        try:
            self.ConfigDic["Segundo_Mensaje"] = self.config.getboolean("Widgets","Segundo_Mensaje")
        except Exception:
            pass
        try:
            self.ConfigDic["Ubicacion_Mensajes2"] =  [self.config.getfloat("Widgets","Ubicacion_Mensajes2_relx"),self.config.getfloat("Widgets","Ubicacion_Mensajes2_rely"),self.config.get("Widgets","Ubicacion_Mensajes2_anchor")]
        except Exception:
            pass
        try:
            self.ConfigDic["Color_Mensajes2"] = self.config.get("Widgets","Color_Mensajes2")
            if self.ConfigDic["Color_Mensajes2"] == "#000001":
                self.ConfigDic["Color_Mensajes2"] = "#000000"
        except Exception:
            pass
        try:
            self.ConfigDic["Letra_Mensajes2"] = self.config.get("Widgets","Letra_Mensajes2")
        except Exception:
            pass
        try:
            self.ConfigDic["Tamannio_Mensajes2"] = self.config.getint("Widgets","Tamannio_Mensajes2")
        except Exception:
            pass
        try:
            self.ConfigDic["Calendario"] = self.config.getboolean("Widgets","Calendario")
        except Exception:
            pass
        try:
            self.ConfigDic["Ubicacion_Calendario"] =  [self.config.getfloat("Widgets","Ubicacion_Calendario_relx"),self.config.getfloat("Widgets","Ubicacion_Calendario_rely"),self.config.get("Widgets","Ubicacion_Calendario_anchor")]
        except Exception:
            pass
        try:
            self.ConfigDic["Color_Calendario"] = self.config.get("Widgets","Color_Calendario")
            if self.ConfigDic["Color_Calendario"] == "#000001":
                self.ConfigDic["Color_Calendario"] = "#000000"
        except Exception:
            pass
        try:    
            self.ConfigDic["Letra_Calendario"] = self.config.get("Widgets","Letra_Calendario")
        except Exception:
            pass
        try:
            self.ConfigDic["Tamannio_Calendario"] = self.config.getint("Widgets","Tamannio_Calendario")
        except Exception:
            pass
        try:
            self.ConfigDic["Incluir_Semana_Cal"] = self.config.getboolean("Widgets","Incluir_Semana_Cal")
        except Exception:
            pass
        try:
            self.ConfigDic["Color_Mensaje_Dia"] = self.config.get("Widgets","Color_Mensaje_Dia")
            if self.ConfigDic["Color_Mensaje_Dia"] == "#000001":
                self.ConfigDic["Color_Mensaje_Dia"] = "#000000"
        except Exception:
            pass
        try:
            self.ConfigDic["Dia_Mensaje"] = self.config.get("Widgets","Dia_Mensaje")
        except Exception:
            pass
        try:
            self.ConfigDic["Mensaje_Dia"] = self.config.get("Widgets","Mensaje_Dia")
        except Exception:
            pass
        try:
            self.ConfigDic["Mostrar_ayer"] = self.config.getboolean("Widgets","Mostrar_ayer")
        except Exception:
            pass
        try:
            self.ConfigDic["Mostrar_anteayer"] = self.config.getboolean("Widgets","Mostrar_anteayer")
        except Exception:
            pass
        try:
            self.ConfigDic["Click_Cruce"] = self.config.getboolean("Widgets","Click_Cruce")
        except Exception:
            pass
        try:
            self.ConfigDic["Marcar_Dia"] = self.config.getboolean("Widgets","Marcar_Dia")
        except Exception:
            pass
        try:
            self.ConfigDic["Dia_Derecha"] = self.config.get("Widgets","Dia_Derecha")
        except Exception:
            pass
        try:
            self.ConfigDic["Dia_Izquierda"] = self.config.get("Widgets","Dia_Izquierda")
        except Exception:
            pass
        try:
            with open("cruce.set", encoding="utf-8") as Archivo_Cruce:
                for linea in Archivo_Cruce:
                    if linea.startswith('True'):
                        self.ConfigDic["Cruce_Monitor"] = True
        except Exception:
            pass
        #Formateo de variables para widget Mensaje del Día (Soporta mostrar solo los de hoy, hoy + ayer y hoy mas ayer mas anteayer):
        self.ahora_dia = str(str(self.ahora.year)+"-"+str(self.ahora.month)+"-"+str(self.ahora.day))
        self.ayer_dia = str(str(self.ayer.year)+"-"+str(self.ayer.month)+"-"+str(self.ayer.day))
        self.anteayer_dia = str(str(self.anteayer.year)+"-"+str(self.anteayer.month)+"-"+str(self.anteayer.day))
        if self.ConfigDic["Mostrar_anteayer"] == True:
            self.ConfigDic["Mostrar_ayer"] = True
        
        self.RefreshMili = self.ConfigDic["Refresh_Seconds"]*1000


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = crear_ventana(root)
    root.mainloop()