import customtkinter
import datetime
import configparser
import tkinter.font
import os, sys
#import locale
#locale.setlocale(locale.LC_ALL, "es-ES.UTF-8") # Formato local, Ejemplo Español: locale.setlocale(locale.LC_ALL, "es-ES")


class MixatoWidgetsConf:

    def __init__(self, root):
        self.root = root
        self.root.title("Mixato Widgets - Preferencias")
        self.root.iconbitmap("transparente.ico")
        self.root.resizable(False,False)
        if len(sys.argv) == 2:
            self.root.geometry(sys.argv[1])
        self.Cargar_Configuración()
        self.Configurar_Ventana()

    def Cargar_Configuración(self):
        # Configuración default
        self.Textos = {"Monitor_Widget" : 0} # Inicio diccionario para generar textos
        self.ConfigDic = {"Monitor_Widget" : 0} # Se elige el monitor enumerados de izq a der, empezando por 0
        self.ConfigDic["Full_Derecha"] = False # Manda todo a la derecha si tengo 3 monitores
        self.ConfigDic["Click_Cruce"] = False
        self.ConfigDic["Modo_Oscuro"] = False
        self.ConfigDic["Solo_Hora"] = False
        self.ConfigDic["Alpha"] = 1
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
            self.ConfigDic["Solo_Hora"] = self.config.getboolean("Widgets","Solo_Hora")
        except Exception:
            pass
        try:
            self.ConfigDic["Alpha"] = self.config.get("Widgets","Alpha")
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
        self.reajustar_ubicaciones()

    def reajustar_ubicaciones(self):
        self.ConfigDic["Ubicacion_Hora_relx"] = self.ConfigDic["Ubicacion_Hora"][0]
        self.ConfigDic["Ubicacion_Hora_rely"] = self.ConfigDic["Ubicacion_Hora"][1]
        self.ConfigDic["Ubicacion_Hora_anchor"] = self.ConfigDic["Ubicacion_Hora"][2]
        self.ConfigDic["Ubicacion_Fecha_relx"] = self.ConfigDic["Ubicacion_Fecha"][0]
        self.ConfigDic["Ubicacion_Fecha_rely"] = self.ConfigDic["Ubicacion_Fecha"][1]
        self.ConfigDic["Ubicacion_Fecha_anchor"] = self.ConfigDic["Ubicacion_Fecha"][2]
        self.ConfigDic["Ubicacion_Mensajes_relx"] = self.ConfigDic["Ubicacion_Mensajes"][0]
        self.ConfigDic["Ubicacion_Mensajes_rely"] = self.ConfigDic["Ubicacion_Mensajes"][1]
        self.ConfigDic["Ubicacion_Mensajes_anchor"] = self.ConfigDic["Ubicacion_Mensajes"][2]
        self.ConfigDic["Ubicacion_Mensajes2_relx"] = self.ConfigDic["Ubicacion_Mensajes2"][0]
        self.ConfigDic["Ubicacion_Mensajes2_rely"] = self.ConfigDic["Ubicacion_Mensajes2"][1]
        self.ConfigDic["Ubicacion_Mensajes2_anchor"] = self.ConfigDic["Ubicacion_Mensajes2"][2]
        self.ConfigDic["Ubicacion_Calendario_relx"] = self.ConfigDic["Ubicacion_Calendario"][0]
        self.ConfigDic["Ubicacion_Calendario_rely"] = self.ConfigDic["Ubicacion_Calendario"][1]
        self.ConfigDic["Ubicacion_Calendario_anchor"] = self.ConfigDic["Ubicacion_Calendario"][2]    

    def Configurar_Ventana(self):
        self.tipos_letra = tkinter.font.families()
        self.tipos_letra = sorted(self.tipos_letra)
        self.Frame_General = customtkinter.CTkFrame(self.root)
        self.Frame_General.grid(row=1, column=0)
        self.tabview = customtkinter.CTkTabview(self.Frame_General, anchor="w")
        self.tabview.pack(fill="both", expand=True)
        self.Marco_Inicial(0,0)
        self.tabview.add("Fecha y Hora")
        self.Marco_Hora(1,0)
        self.Marco_Fecha(1,1)
        self.tabview.add("Calendario")
        self.Marco_Calendario(2,0)
        self.tabview.add("Mensajes")
        self.Marco_Mensajes(3,0)
        self.Marco_Mensajes2(3,1)
        self.Marco_Final(10,0)

    def Marco_Inicial(self, fila, columna):
        self.Frame_Inicial = customtkinter.CTkFrame(self.root)
        self.Frame_Inicial.grid(row=fila, column=columna, columnspan=6)
        Label_Monitor=customtkinter.CTkLabel(self.Frame_Inicial, text="Monitor:")
        Label_Monitor.grid(row=0, column=0, padx=5, pady=5)
        self.Textos["Monitor_Widget"] = self.Generar_Texto("Monitor_Widget",self.Frame_Inicial)
        self.Textos["Monitor_Widget"].grid(row=0, column=1, padx=5, pady=5)
        Label_Full_Derecha=customtkinter.CTkLabel(self.Frame_Inicial, text="Full Derecha:")
        Label_Full_Derecha.grid(row=0, column=2, padx=5, pady=5)
        self.Desplegable_FDerecha = self.Generar_Desplegable_bool("Full_Derecha",self.Frame_Inicial, ["True", "False"])
        self.Desplegable_FDerecha.grid(row=0, column=3, padx=5, pady=5)    
        Label_Modo_Oscuro=customtkinter.CTkLabel(self.Frame_Inicial, text="Modo Oscuro:")
        Label_Modo_Oscuro.grid(row=1, column=0, padx=5, pady=5)
        self.Desplegable_MOscuro = self.Generar_Desplegable_bool("Modo_Oscuro",self.Frame_Inicial, ["True", "False"])
        self.Desplegable_MOscuro.grid(row=1, column=1, padx=5, pady=5)   
        Label_Refresh=customtkinter.CTkLabel(self.Frame_Inicial, text="Segundos Refresh:")
        Label_Refresh.grid(row=1, column=2, padx=5, pady=5)
        self.Textos["Refresh_Seconds"] = self.Generar_Texto("Refresh_Seconds",self.Frame_Inicial)
        self.Textos["Refresh_Seconds"].grid(row=1, column=3, padx=5, pady=5) 
        Label_Alpha=customtkinter.CTkLabel(self.Frame_Inicial, text="Transparencia:")
        Label_Alpha.grid(row=2, column=0, padx=5, pady=5)
        self.Textos["Alpha"] = self.Generar_Texto("Alpha",self.Frame_Inicial)
        self.Textos["Alpha"].grid(row=2, column=1, padx=5, pady=5) 
        Label_Fecha_Hora=customtkinter.CTkLabel(self.Frame_Inicial, text="Solo Fecha y Hora:")
        Label_Fecha_Hora.grid(row=2, column=2, padx=5, pady=5)
        self.Desplegable_Fecha_Hora = self.Generar_Desplegable_bool("Solo_Hora",self.Frame_Inicial, ["True", "False"])
        self.Desplegable_Fecha_Hora.grid(row=2, column=3, padx=5, pady=5)  

    def Marco_Hora(self, fila, columna):  
        self.Frame_Hora = customtkinter.CTkFrame(self.tabview.tab("Fecha y Hora"))
        self.Frame_Hora.grid(row=fila, column=columna)
        Label_Hora=customtkinter.CTkLabel(self.Frame_Hora, text="Mostrar Hora:")
        Label_Hora.grid(row=0, column=0, padx=5, pady=5)
        self.Desplegable_Hora = self.Generar_Desplegable_bool("Hora",self.Frame_Hora, ["True", "False"])
        self.Desplegable_Hora.grid(row=0, column=1, padx=5, pady=5)
        Label_relx_Hora=customtkinter.CTkLabel(self.Frame_Hora, text="Ubicación Hora X:")
        Label_relx_Hora.grid(row=1, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Hora_relx"] = self.Generar_Texto("Ubicacion_Hora_relx",self.Frame_Hora)
        self.Textos["Ubicacion_Hora_relx"].grid(row=1, column=1, padx=5, pady=5)        
        Label_rely_Hora=customtkinter.CTkLabel(self.Frame_Hora, text="Ubicación Hora Y:")
        Label_rely_Hora.grid(row=2, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Hora_rely"] = self.Generar_Texto("Ubicacion_Hora_rely",self.Frame_Hora)
        self.Textos["Ubicacion_Hora_rely"].grid(row=2, column=1, padx=5, pady=5)
        Label_anchor_Hora=customtkinter.CTkLabel(self.Frame_Hora, text="Ubicación Hora Anchor:")
        Label_anchor_Hora.grid(row=3, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Hora_anchor"] = self.Generar_Texto("Ubicacion_Hora_anchor",self.Frame_Hora)
        self.Textos["Ubicacion_Hora_anchor"].grid(row=3, column=1, padx=5, pady=5)
        Label_Color_Hora=customtkinter.CTkLabel(self.Frame_Hora, text="Color Hora:")
        Label_Color_Hora.grid(row=4, column=0, padx=5, pady=5)
        self.Textos["Color_Hora"] = self.Generar_Texto("Color_Hora",self.Frame_Hora)
        self.Textos["Color_Hora"].grid(row=4, column=1, padx=5, pady=5)
        Label_Letra_Hora=customtkinter.CTkLabel(self.Frame_Hora, text="Letra Hora:")
        Label_Letra_Hora.grid(row=5, column=0, padx=5, pady=5)
        self.Desplegable_Letra_Hora = self.Generar_Desplegable("Letra_Hora",self.Frame_Hora, self.tipos_letra)
        self.Desplegable_Letra_Hora.grid(row=5, column=1, padx=5, pady=5)
        Label_Tamannio_Hora=customtkinter.CTkLabel(self.Frame_Hora, text="Tamaño Hora:")
        Label_Tamannio_Hora.grid(row=6, column=0, padx=5, pady=5)
        self.Textos["Tamannio_Hora"] = self.Generar_Texto("Tamannio_Hora",self.Frame_Hora)
        self.Textos["Tamannio_Hora"].grid(row=6, column=1, padx=5, pady=5)
        Label_Color_Mensaje_Dia=customtkinter.CTkLabel(self.Frame_Hora, text="Color Mensaje del Día:")
        Label_Color_Mensaje_Dia.grid(row=7, column=0, padx=5, pady=5)
        self.Textos["Color_Mensaje_Dia"] = self.Generar_Texto("Color_Mensaje_Dia",self.Frame_Hora)
        self.Textos["Color_Mensaje_Dia"].grid(row=7, column=1, padx=5, pady=5)
        Label_Mostrar_Ayer=customtkinter.CTkLabel(self.Frame_Hora, text="Mostrar Ayer:")
        Label_Mostrar_Ayer.grid(row=8, column=0, padx=5, pady=5)
        self.Desplegable_Mostrar_Ayer = self.Generar_Desplegable_bool("Mostrar_ayer",self.Frame_Hora, ["True", "False"])
        self.Desplegable_Mostrar_Ayer.grid(row=8, column=1, padx=5, pady=5)

    def Marco_Fecha(self, fila, columna):
        self.Frame_Fecha = customtkinter.CTkFrame(self.tabview.tab("Fecha y Hora"))
        self.Frame_Fecha.grid(row=fila, column=columna)
        Label_Fecha=customtkinter.CTkLabel(self.Frame_Fecha, text="Mostrar Fecha:")
        Label_Fecha.grid(row=0, column=0, padx=5, pady=5)
        self.Desplegable_Fecha = self.Generar_Desplegable_bool("Fecha",self.Frame_Fecha, ["True", "False"])
        self.Desplegable_Fecha.grid(row=0, column=1, padx=5, pady=5)
        Label_relx_Fecha=customtkinter.CTkLabel(self.Frame_Fecha, text="Ubicación Fecha X:")
        Label_relx_Fecha.grid(row=1, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Fecha_relx"] = self.Generar_Texto("Ubicacion_Fecha_relx",self.Frame_Fecha)
        self.Textos["Ubicacion_Fecha_relx"].grid(row=1, column=1, padx=5, pady=5)
        Label_rely_Fecha=customtkinter.CTkLabel(self.Frame_Fecha, text="Ubicación Fecha Y:")
        Label_rely_Fecha.grid(row=2, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Fecha_rely"] = self.Generar_Texto("Ubicacion_Fecha_rely",self.Frame_Fecha)
        self.Textos["Ubicacion_Fecha_rely"].grid(row=2, column=1, padx=5, pady=5)
        Label_anchor_Fecha=customtkinter.CTkLabel(self.Frame_Fecha, text="Ubicación Fecha Anchor:")
        Label_anchor_Fecha.grid(row=3, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Fecha_anchor"] = self.Generar_Texto("Ubicacion_Fecha_anchor",self.Frame_Fecha)
        self.Textos["Ubicacion_Fecha_anchor"].grid(row=3, column=1, padx=5, pady=5)
        Label_Color_Fecha=customtkinter.CTkLabel(self.Frame_Fecha, text="Color Fecha:")
        Label_Color_Fecha.grid(row=4, column=0, padx=5, pady=5)
        self.Textos["Color_Fecha"] = self.Generar_Texto("Color_Fecha",self.Frame_Fecha)
        self.Textos["Color_Fecha"].grid(row=4, column=1, padx=5, pady=5)        
        Label_Letra_Fecha=customtkinter.CTkLabel(self.Frame_Fecha, text="Letra Fecha:")
        Label_Letra_Fecha.grid(row=5, column=0, padx=5, pady=5)
        self.Desplegable_Letra_Fecha = self.Generar_Desplegable("Letra_Fecha",self.Frame_Fecha, self.tipos_letra)
        self.Desplegable_Letra_Fecha.grid(row=5, column=1, padx=5, pady=5)
        Label_Tamannio_Fecha=customtkinter.CTkLabel(self.Frame_Fecha, text="Tamaño Fecha:")
        Label_Tamannio_Fecha.grid(row=6, column=0, padx=5, pady=5)
        self.Textos["Tamannio_Fecha"] = self.Generar_Texto("Tamannio_Fecha",self.Frame_Fecha)
        self.Textos["Tamannio_Fecha"].grid(row=6, column=1, padx=5, pady=5)
        Label_Semana=customtkinter.CTkLabel(self.Frame_Fecha, text="Mostrar Semana:")
        Label_Semana.grid(row=7, column=0, padx=5, pady=5)
        self.Desplegable_semana = self.Generar_Desplegable_bool("Incluir_Semana",self.Frame_Fecha, ["True", "False"])
        self.Desplegable_semana.grid(row=7, column=1, padx=5, pady=5) 
        Label_Mostrar_Anteayer=customtkinter.CTkLabel(self.Frame_Fecha, text="Mostrar Anteayer:")
        Label_Mostrar_Anteayer.grid(row=8, column=0, padx=5, pady=5)
        self.Desplegable_Mostrar_Anteayer = self.Generar_Desplegable_bool("Mostrar_anteayer",self.Frame_Fecha, ["True", "False"])
        self.Desplegable_Mostrar_Anteayer.grid(row=8, column=1, padx=5, pady=5)

    def Marco_Calendario(self, fila, columna):
        self.Frame_Calendario = customtkinter.CTkFrame(self.tabview.tab("Calendario"))
        self.Frame_Calendario.grid(row=fila, column=columna, columnspan=6)
        Label_Calendario=customtkinter.CTkLabel(self.Frame_Calendario, text="Mostrar Calendario:")
        Label_Calendario.grid(row=0, column=0, padx=5, pady=5)
        self.Desplegable_Calendario = self.Generar_Desplegable_bool("Calendario",self.Frame_Calendario, ["True", "False"])
        self.Desplegable_Calendario.grid(row=0, column=1, padx=5, pady=5)
        Label_Letra_Calendario=customtkinter.CTkLabel(self.Frame_Calendario, text="Letra Calendario:")
        Label_Letra_Calendario.grid(row=0, column=2, padx=5, pady=5)
        self.Desplegable_Letra_Calendario = self.Generar_Desplegable("Letra_Calendario",self.Frame_Calendario, self.tipos_letra)
        self.Desplegable_Letra_Calendario.grid(row=0, column=3, padx=5, pady=5)
        Label_relx_Calendario=customtkinter.CTkLabel(self.Frame_Calendario, text="Ubicación Calendario X:")
        Label_relx_Calendario.grid(row=1, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Calendario_relx"] = self.Generar_Texto("Ubicacion_Calendario_relx",self.Frame_Calendario)
        self.Textos["Ubicacion_Calendario_relx"].grid(row=1, column=1, padx=5, pady=5)        
        Label_rely_Calendario=customtkinter.CTkLabel(self.Frame_Calendario, text="Ubicación Calendario Y:")
        Label_rely_Calendario.grid(row=1, column=2, padx=5, pady=5)
        self.Textos["Ubicacion_Calendario_rely"] = self.Generar_Texto("Ubicacion_Calendario_rely",self.Frame_Calendario)
        self.Textos["Ubicacion_Calendario_rely"].grid(row=1, column=3, padx=5, pady=5)
        Label_anchor_Calendario=customtkinter.CTkLabel(self.Frame_Calendario, text="Ubicación Calendario Anchor:")
        Label_anchor_Calendario.grid(row=2, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Calendario_anchor"] = self.Generar_Texto("Ubicacion_Calendario_anchor",self.Frame_Calendario)
        self.Textos["Ubicacion_Calendario_anchor"].grid(row=2, column=1, padx=5, pady=5)    
        Label_Color_Calendario=customtkinter.CTkLabel(self.Frame_Calendario, text="Color Calendario:")
        Label_Color_Calendario.grid(row=2, column=2, padx=5, pady=5)
        self.Textos["Color_Calendario"] = self.Generar_Texto("Color_Calendario",self.Frame_Calendario)
        self.Textos["Color_Calendario"].grid(row=2, column=3, padx=5, pady=5)
        Label_Letra_Calendario=customtkinter.CTkLabel(self.Frame_Calendario, text="Letra Calendario:")
        Label_Letra_Calendario.grid(row=3, column=0, padx=5, pady=5)
        self.Desplegable_Letra_Calendario = self.Generar_Desplegable("Letra_Calendario",self.Frame_Calendario, self.tipos_letra)
        self.Desplegable_Letra_Calendario.grid(row=3, column=1, padx=5, pady=5)
        Label_Tamannio_Calendario=customtkinter.CTkLabel(self.Frame_Calendario, text="Tamaño Calendario:")
        Label_Tamannio_Calendario.grid(row=3, column=2, padx=5, pady=5)
        self.Textos["Tamannio_Calendario"] = self.Generar_Texto("Tamannio_Calendario",self.Frame_Calendario)
        self.Textos["Tamannio_Calendario"].grid(row=3, column=3, padx=5, pady=5)
        Label_Semana_Cal=customtkinter.CTkLabel(self.Frame_Calendario, text="Incluir Semana:")
        Label_Semana_Cal.grid(row=4, column=0, padx=5, pady=5)
        self.Desplegable_Semana_Cal = self.Generar_Desplegable_bool("Incluir_Semana_Cal",self.Frame_Calendario, ["True", "False"])
        self.Desplegable_Semana_Cal.grid(row=4, column=1, padx=5, pady=5)
        Label_Marcar_Dia=customtkinter.CTkLabel(self.Frame_Calendario, text="Marcar Día:")
        Label_Marcar_Dia.grid(row=4, column=2, padx=5, pady=5)
        self.Desplegable_Marcar_Dia = self.Generar_Desplegable_bool("Marcar_Dia",self.Frame_Calendario, ["True", "False"])
        self.Desplegable_Marcar_Dia.grid(row=4, column=3, padx=5, pady=5)
        Label_Dia_Izquierda=customtkinter.CTkLabel(self.Frame_Calendario, text="Marca Día Izquierda:")
        Label_Dia_Izquierda.grid(row=5, column=0, padx=5, pady=5)
        self.Textos["Dia_Izquierda"] = self.Generar_Texto("Dia_Izquierda",self.Frame_Calendario)
        self.Textos["Dia_Izquierda"].grid(row=5, column=1, padx=5, pady=5)
        Label_Dia_Derecha=customtkinter.CTkLabel(self.Frame_Calendario, text="Marca Día Derecha:")
        Label_Dia_Derecha.grid(row=5, column=2, padx=5, pady=5)
        self.Textos["Dia_Derecha"] = self.Generar_Texto("Dia_Derecha",self.Frame_Calendario)
        self.Textos["Dia_Derecha"].grid(row=5, column=3, padx=5, pady=5)

    def Marco_Mensajes(self, fila, columna):
        self.Frame_Mensajes = customtkinter.CTkFrame(self.tabview.tab("Mensajes"))
        self.Frame_Mensajes.grid(row=fila, column=columna)
        Label_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes, text="Mostrar Mensajes 1:")
        Label_Mensajes.grid(row=0, column=0, padx=5, pady=5)
        self.Desplegable_Mensajes = self.Generar_Desplegable_bool("Mensajes",self.Frame_Mensajes, ["True", "False"])
        self.Desplegable_Mensajes.grid(row=0, column=1, padx=5, pady=5)
        Label_relx_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes, text="Ubicación Mensajes X:")
        Label_relx_Mensajes.grid(row=1, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Mensajes_relx"] = self.Generar_Texto("Ubicacion_Mensajes_relx",self.Frame_Mensajes)
        self.Textos["Ubicacion_Mensajes_relx"].grid(row=1, column=1, padx=5, pady=5)        
        Label_rely_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes, text="Ubicación Mensajes Y:")
        Label_rely_Mensajes.grid(row=2, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Mensajes_rely"] = self.Generar_Texto("Ubicacion_Mensajes_rely",self.Frame_Mensajes)
        self.Textos["Ubicacion_Mensajes_rely"].grid(row=2, column=1, padx=5, pady=5)
        Label_anchor_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes, text="Ubicación Mensajes Anchor:")
        Label_anchor_Mensajes.grid(row=3, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Mensajes_anchor"] = self.Generar_Texto("Ubicacion_Mensajes_anchor",self.Frame_Mensajes)
        self.Textos["Ubicacion_Mensajes_anchor"].grid(row=3, column=1, padx=5, pady=5)
        Label_Color_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes, text="Color Mensajes:")
        Label_Color_Mensajes.grid(row=4, column=0, padx=5, pady=5)
        self.Textos["Color_Mensajes"] = self.Generar_Texto("Color_Mensajes",self.Frame_Mensajes)
        self.Textos["Color_Mensajes"].grid(row=4, column=1, padx=5, pady=5)
        Label_Letra_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes, text="Letra Mensajes:")
        Label_Letra_Mensajes.grid(row=5, column=0, padx=5, pady=5)
        self.Desplegable_Letra_Mensajes = self.Generar_Desplegable("Letra_Mensajes",self.Frame_Mensajes, self.tipos_letra)
        self.Desplegable_Letra_Mensajes.grid(row=5, column=1, padx=5, pady=5)
        Label_Tamannio_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes, text="Tamaño Mensajes:")
        Label_Tamannio_Mensajes.grid(row=6, column=0, padx=5, pady=5)
        self.Textos["Tamannio_Mensajes"] = self.Generar_Texto("Tamannio_Mensajes",self.Frame_Mensajes)
        self.Textos["Tamannio_Mensajes"].grid(row=6, column=1, padx=5, pady=5)

    def Marco_Mensajes2(self, fila, columna):
        self.Frame_Mensajes2 = customtkinter.CTkFrame(self.tabview.tab("Mensajes"))
        self.Frame_Mensajes2.grid(row=fila, column=columna)
        Label_Mensajes2=customtkinter.CTkLabel(self.Frame_Mensajes2, text="Mostrar Mensajes 2:")
        Label_Mensajes2.grid(row=0, column=0, padx=5, pady=5)
        self.Desplegable_Mensajes2 = self.Generar_Desplegable_bool("Segundo_Mensaje",self.Frame_Mensajes2, ["True", "False"])
        self.Desplegable_Mensajes2.grid(row=0, column=1, padx=5, pady=5)
        Label_relx_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes2, text="Ubicación Mensajes 2 X:")
        Label_relx_Mensajes.grid(row=1, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Mensajes2_relx"] = self.Generar_Texto("Ubicacion_Mensajes2_relx",self.Frame_Mensajes2)
        self.Textos["Ubicacion_Mensajes2_relx"].grid(row=1, column=1, padx=5, pady=5)        
        Label_rely_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes2, text="Ubicación Mensajes 2 Y:")
        Label_rely_Mensajes.grid(row=2, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Mensajes2_rely"] = self.Generar_Texto("Ubicacion_Mensajes2_rely",self.Frame_Mensajes2)
        self.Textos["Ubicacion_Mensajes2_rely"].grid(row=2, column=1, padx=5, pady=5)
        Label_anchor_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes2, text="Ubicación Mensajes 2 Anchor:")
        Label_anchor_Mensajes.grid(row=3, column=0, padx=5, pady=5)
        self.Textos["Ubicacion_Mensajes2_anchor"] = self.Generar_Texto("Ubicacion_Mensajes2_anchor",self.Frame_Mensajes2)
        self.Textos["Ubicacion_Mensajes2_anchor"].grid(row=3, column=1, padx=5, pady=5)
        Label_Color_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes2, text="Color Mensajes 2:")
        Label_Color_Mensajes.grid(row=4, column=0, padx=5, pady=5)
        self.Textos["Color_Mensajes2"] = self.Generar_Texto("Color_Mensajes2",self.Frame_Mensajes2)
        self.Textos["Color_Mensajes2"].grid(row=4, column=1, padx=5, pady=5)
        Label_Letra_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes2, text="Letra Mensajes 2:")
        Label_Letra_Mensajes.grid(row=5, column=0, padx=5, pady=5)
        self.Desplegable_Letra_Mensajes = self.Generar_Desplegable("Letra_Mensajes2",self.Frame_Mensajes2, self.tipos_letra)
        self.Desplegable_Letra_Mensajes.grid(row=5, column=1, padx=5, pady=5)
        Label_Tamannio_Mensajes=customtkinter.CTkLabel(self.Frame_Mensajes2, text="Tamaño Mensajes 2:")
        Label_Tamannio_Mensajes.grid(row=6, column=0, padx=5, pady=5)
        self.Textos["Tamannio_Mensajes2"] = self.Generar_Texto("Tamannio_Mensajes2",self.Frame_Mensajes2)
        self.Textos["Tamannio_Mensajes2"].grid(row=6, column=1, padx=5, pady=5)

    def Marco_Final(self, fila, columna):
        self.Frame_Final = customtkinter.CTkFrame(self.root)
        self.Frame_Final.grid(row=fila, column=columna, columnspan=5)
        boton_guardar = customtkinter.CTkButton(self.Frame_Final, text="Guardar", command=self.Guardar_Configuración)
        boton_guardar.grid(row=0, column=1, padx=5, pady=5)
        boton_Mensajes = customtkinter.CTkButton(self.Frame_Final, text="Abrir Mensajes", command= self.Lanzar_txt)
        boton_Mensajes.grid(row=0, column=2, padx=5, pady=5)
        boton_cerrar = customtkinter.CTkButton(self.Frame_Final, text="Cerrar", command=self.Cerrar_Soft)
        boton_cerrar.grid(row=0, column=3, padx=5, pady=5)

    def Generar_Desplegable_bool(self,clave, destino, valores):
        devolver = customtkinter.CTkComboBox(destino, values=valores, state="readonly", command=lambda valor: self.obtener_valor(valor, clave))
        devolver.set(self.traducir_bool(self.ConfigDic[clave]))
        return(devolver)
    
    def Generar_Desplegable(self,clave, destino, valores):
        devolver = customtkinter.CTkComboBox(destino, values=valores, state="readonly", command=lambda valor: self.obtener_valor(valor, clave))
        devolver.set(self.ConfigDic[clave])
        return(devolver)

    def obtener_valor(self, valor, clave):
        self.ConfigDic[clave] = valor
        self.config.set("Widgets", clave, self.ConfigDic[clave])

    def Generar_Texto(self, clave, destino):
        devolver = customtkinter.CTkEntry(destino)
        devolver.insert(0, self.ConfigDic[clave])
        return(devolver)

    def obtener_texto(self):
        for clave, widget in self.Textos.items():
            self.ConfigDic[clave]=widget.get()
            self.config.set("Widgets",clave,self.ConfigDic[clave])

    def traducir_bool(self, bool):
        if bool:
            return("True")
        return("False")
    
    def Guardar_Configuración(self):
            self.obtener_texto()
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
            with open('reload.set', 'w') as Archivo_Reload:
                Archivo_Reload.write('True')

    def Lanzar_txt(self):
        script_path = os.path.abspath('messages.txt') # Obtiene la ruta absoluta
        os.startfile(script_path)

    def Cerrar_Soft(self):
        with open('cerrar.txt','w') as Archivo_Cerrar:
            Archivo_Cerrar.write('True')



if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")
    root = customtkinter.CTk()
    app = MixatoWidgetsConf(root)
    root.mainloop()