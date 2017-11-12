'''
Created on 11 nov. 2017

@author: tecuapan
'''
import wx
import wx.xrc
from Principal import *
import pickle
###########################################################################
'''
Indice GUI
    1 Objeto1 Limpiar texto
    2 Objeto2 Vectorizacion del modelo
    3 Objeto3 Matriz del vector
    4 Objeto4 Generar Modelo
    5 Objeto5 Clasificar
    6 Objeto6 Cargar modelo
    7 Objeto7 Teoria basica
Variables globales
    i encargada de seleccionar ventanas se inicializa con funcion Seleccion_de_Ventanas
    j se encarga de finalizar el programa se inicializa con la funcion Mata_Programa_Definitivo
Funciones propios de GUI
    Seleccion_de_Ventanas
    Mata_Programa_Definitivo
'''
#################################################################################################
global i
i=1
global j
j=True
#################################################################################################
def Seleccion_de_Ventanas(opcion):
    global i
    i=opcion
#################################################################################################
def Mata_Programa_Definitivo(opcion):
    global j
    j=opcion
#################################################################################################
###########################################################################
## Class Objeto1
###########################################################################
class Objeto1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistema de sugerencias", pos = wx.DefaultPosition, size = wx.Size( 683,384 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.Centre(True)
        self.Show()
        self.Bind(wx.EVT_CLOSE, self.onClose)

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Limpiar texto", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem1 )
        
        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Vectorizacion de Modelo", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem2 )
        
        self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Matriz del vector", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem3 )
        
        self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Generar Modelo", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem4 )
        
        self.m_menubar1.Append( self.m_menu1, u"Crear modelo" ) 
        
        self.m_menu2 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Cargar modelo y clasificar", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem5 )
        
        self.m_menuItem6 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Especificaciones de modelo", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem6 )
        
        self.m_menubar1.Append( self.m_menu2, u"Clasificar modelo" ) 
        
        self.m_menu3 = wx.Menu()
        self.m_menuItem7 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Teoria basica", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem7 )
        
        self.m_menuItem8 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Contacto", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem8 )
        
        self.m_menubar1.Append( self.m_menu3, u"Ayuda" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        gSizer7 = wx.GridSizer( 4, 1, 0, 0 )
        
        bSizer14 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer18 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Rutas de archivos para generar modelos" ), wx.VERTICAL )
        
        gSizer9 = wx.GridSizer( 2, 2, 0, 0 )
        
        bSizer20 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText5 = wx.StaticText( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Archivos para la creacion del modelo", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer20.Add( self.m_staticText5, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticline5 = wx.StaticLine( sbSizer18.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.m_staticline5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
        self.m_staticline5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        bSizer20.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        gSizer9.Add( bSizer20, 1, wx.EXPAND, 5 )
        
        bSizer21 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText6 = wx.StaticText( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Archivos para  probar modelo", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer21.Add( self.m_staticText6, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticline6 = wx.StaticLine( sbSizer18.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer21.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        gSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )
        
        bSizer22 = wx.BoxSizer( wx.VERTICAL )
        
        self.Entrada = wx.TextCtrl( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Ejemplo C:/User/Desktop/Mi_Carpeta_Base", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer22.Add( self.Entrada, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer9.Add( bSizer22, 1, wx.EXPAND, 5 )
        
        bSizer23 = wx.BoxSizer( wx.VERTICAL )
        
        self.Evaluacion = wx.TextCtrl( sbSizer18.GetStaticBox(), wx.ID_ANY, u"Ejemplo C:/User/Desktop/Mi_Carpeta_Evaluacion", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.Evaluacion, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer9.Add( bSizer23, 1, wx.EXPAND, 5 )
        
        
        sbSizer18.Add( gSizer9, 1, wx.EXPAND, 5 )
        
        
        bSizer14.Add( sbSizer18, 1, wx.EXPAND, 1 )
        
        
        gSizer7.Add( bSizer14, 1, wx.EXPAND, 5 )
        
        bSizer16 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer181 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Rutas de archivos limpios para modelo" ), wx.VERTICAL )
        
        gSizer91 = wx.GridSizer( 2, 2, 0, 0 )
        
        bSizer201 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText51 = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"Archivos limpios para la creacion del modelo", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText51.Wrap( -1 )
        bSizer201.Add( self.m_staticText51, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticline51 = wx.StaticLine( sbSizer181.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.m_staticline51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
        self.m_staticline51.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        bSizer201.Add( self.m_staticline51, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        gSizer91.Add( bSizer201, 1, wx.EXPAND, 5 )
        
        bSizer211 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText61 = wx.StaticText( sbSizer181.GetStaticBox(), wx.ID_ANY, u"Archivos limpios para  probar modelo", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61.Wrap( -1 )
        bSizer211.Add( self.m_staticText61, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticline61 = wx.StaticLine( sbSizer181.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer211.Add( self.m_staticline61, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        gSizer91.Add( bSizer211, 1, wx.EXPAND, 5 )
        
        bSizer221 = wx.BoxSizer( wx.VERTICAL )
        
        self.Entrada_Limpia = wx.TextCtrl( sbSizer181.GetStaticBox(), wx.ID_ANY, u"Ejemplo C:/User/Desktop/Mi_Carpeta_Base", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer221.Add( self.Entrada_Limpia, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer91.Add( bSizer221, 1, wx.EXPAND, 5 )
        
        bSizer231 = wx.BoxSizer( wx.VERTICAL )
        
        self.Evaluacion_Limpia = wx.TextCtrl( sbSizer181.GetStaticBox(), wx.ID_ANY, u"Ejemplo C:/User/Desktop/Mi_Carpeta_Evaluacion", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer231.Add( self.Evaluacion_Limpia, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer91.Add( bSizer231, 1, wx.EXPAND, 5 )
        
        
        sbSizer181.Add( gSizer91, 1, wx.EXPAND, 5 )
        
        
        bSizer16.Add( sbSizer181, 1, wx.EXPAND, 5 )
        
        
        gSizer7.Add( bSizer16, 1, wx.EXPAND, 5 )
        
        bSizer18 = wx.BoxSizer( wx.VERTICAL )
        
        gSizer13 = wx.GridSizer( 2, 2, 0, 0 )
        
        bSizer36 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer36.SetMinSize( wx.Size( -1,-10 ) ) 
        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Sucio", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )
        bSizer36.Add( self.m_staticText21, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        gSizer13.Add( bSizer36, 1, wx.EXPAND, 0 )
        
        bSizer37 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Limpio", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )
        bSizer37.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        gSizer13.Add( bSizer37, 1, wx.EXPAND, 5 )
        
        bSizer38 = wx.BoxSizer( wx.VERTICAL )
        
        self.Texto_sucio = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer38.Add( self.Texto_sucio, 1, wx.EXPAND|wx.RIGHT, 5 )
        
        
        gSizer13.Add( bSizer38, 1, wx.EXPAND, 5 )
        
        bSizer39 = wx.BoxSizer( wx.VERTICAL )
        
        self.Texto_limpio = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer39.Add( self.Texto_limpio, 1, wx.EXPAND, 5 )
        
        
        gSizer13.Add( bSizer39, 1, wx.EXPAND, 5 )
        
        
        bSizer18.Add( gSizer13, 1, wx.EXPAND, 5 )
        
        
        gSizer7.Add( bSizer18, 1, wx.EXPAND, 5 )
        
        bSizer19 = wx.BoxSizer( wx.VERTICAL )
        
        gSizer14 = wx.GridSizer( 1, 3, 0, 0 )
        
        bSizer40 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Estado del programa" ), wx.VERTICAL )
        
        self.Porcentaje = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Esperando ejecucion", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer23.Add( self.Porcentaje, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.Barrita = wx.Gauge( sbSizer23.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.Barrita.SetValue( 0 ) 
        sbSizer23.Add( self.Barrita, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer40.Add( sbSizer23, 1, wx.EXPAND, 5 )
        
        
        gSizer14.Add( bSizer40, 1, wx.EXPAND, 5 )
        
        bSizer41 = wx.BoxSizer( wx.VERTICAL )
        
        self.Iniciar_Proceso = wx.Button( self, wx.ID_ANY, u"Iniciar proceso", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer41.Add( self.Iniciar_Proceso, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        
        gSizer14.Add( bSizer41, 1, wx.EXPAND, 5 )
        
        bSizer42 = wx.BoxSizer( wx.VERTICAL )
        
        self.Siguiente_proceso = wx.Button( self, wx.ID_ANY, u"Siguiente proceso", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer42.Add( self.Siguiente_proceso, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer14.Add( bSizer42, 1, wx.EXPAND, 5 )
        
        
        bSizer19.Add( gSizer14, 1, wx.EXPAND, 5 )
        
        
        gSizer7.Add( bSizer19, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( gSizer7 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_MENU, self.Limpiar_texto, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.Vectorizacion_modelo, id = self.m_menuItem2.GetId() )
        self.Bind( wx.EVT_MENU, self.Valor_numerico_vector, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.Generar_modelo, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.Clasificar, id = self.m_menuItem5.GetId() )
        self.Bind( wx.EVT_MENU, self.Especificaciones_modelo, id = self.m_menuItem6.GetId() )
        self.Bind( wx.EVT_MENU, self.Teoria_basica, id = self.m_menuItem7.GetId() )
        self.Bind( wx.EVT_MENU, self.Contacto, id = self.m_menuItem8.GetId() )
        self.Iniciar_Proceso.Bind( wx.EVT_BUTTON, self.Iniciar )
        self.Siguiente_proceso.Bind( wx.EVT_BUTTON, self.next )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def Limpiar_texto( self, event ):
        Seleccion_de_Ventanas(1)
        self.Destroy()
    
    def Vectorizacion_modelo( self, event ):
        Seleccion_de_Ventanas(2)
        self.Destroy()
    
    def Valor_numerico_vector( self, event ):
        Seleccion_de_Ventanas(3)
        self.Destroy()
    
    def Generar_modelo( self, event ):
        Seleccion_de_Ventanas(4)
        self.Destroy()
    
    def Clasificar( self, event ):
        Seleccion_de_Ventanas(5)
        self.Destroy()
    
    def Especificaciones_modelo( self, event ):
        Seleccion_de_Ventanas(6)
        self.Destroy()
    
    def Teoria_basica( self, event ):
        Seleccion_de_Ventanas(7)
        self.Destroy()
    
    def Contacto( self, event ):
        Seleccion_de_Ventanas(8)
        self.Destroy()
    
    def onClose(self,event):
        Mata_Programa_Definitivo(False)
        print j
        self.Destroy()
        
    def Iniciar( self, event ):
        c=True
        d=True
        Ruta_entrada = self.Entrada.GetValue()
        Ruta_salida_entrada=self.Entrada_Limpia.GetValue()
        while c:
            sucio,limpio,a,b,c=Generacion_texto_limpiado_pre(Ruta_entrada, Ruta_salida_entrada)
            self.Porcentaje.SetValue(str(a*50/b)+" %")
            self.Texto_sucio.SetValue(sucio)
            self.Texto_limpio.SetValue(limpio)
            self.Barrita.SetValue(int(a*50/b))
        
        Ruta_evaluacion=self.Evaluacion.GetValue()
        Ruta_salida_evaluacion=self.Evaluacion_Limpia.GetValue()
        while d:
            sucio,limpio,a,b,d=Generacion_texto_limpiado_pre(Ruta_evaluacion, Ruta_salida_evaluacion)
            self.Porcentaje.SetValue(str(50+int(a*50/b))+" %")
            self.Texto_sucio.SetValue(sucio)
            self.Texto_limpio.SetValue(limpio)
            self.Barrita.SetValue(50+int(a*50/b))
        
    def next( self, event ):
        Seleccion_de_Ventanas(2)
        self.Destroy()

###########################################################################
## Class Objeto2
###########################################################################

class Objeto2 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistema de sugerencias", pos = wx.DefaultPosition, size = wx.Size( 683,384 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.Centre(True)
        self.Show()
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Limpiar texto", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem1 )
        
        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Vectorizacion de Modelo", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem2 )
        
        self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Matriz del vector", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem3 )
        
        self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Generar Modelo", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem4 )
        
        self.m_menubar1.Append( self.m_menu1, u"Crear modelo" ) 
        
        self.m_menu2 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Cargar modelo y clasificar", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem5 )
        
        self.m_menuItem6 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Especificaciones de modelo", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem6 )
        
        self.m_menubar1.Append( self.m_menu2, u"Clasificar modelo" ) 
        
        self.m_menu3 = wx.Menu()
        self.m_menuItem7 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Teoria basica", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem7 )
        
        self.m_menuItem8 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Contacto", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem8 )
        
        self.m_menubar1.Append( self.m_menu3, u"Ayuda" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        gSizer7 = wx.GridSizer( 4, 1, 0, 0 )
        
        bSizer14 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer1811 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Rutas de archivos limpios para modelo" ), wx.VERTICAL )
        
        gSizer911 = wx.GridSizer( 2, 2, 0, 0 )
        
        bSizer2011 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText511 = wx.StaticText( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"Archivos limpios para la creacion del modelo", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText511.Wrap( -1 )
        bSizer2011.Add( self.m_staticText511, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticline511 = wx.StaticLine( sbSizer1811.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        self.m_staticline511.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
        self.m_staticline511.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        bSizer2011.Add( self.m_staticline511, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        gSizer911.Add( bSizer2011, 1, wx.EXPAND, 5 )
        
        bSizer2111 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText611 = wx.StaticText( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"Archivos limpios para  probar modelo", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText611.Wrap( -1 )
        bSizer2111.Add( self.m_staticText611, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticline611 = wx.StaticLine( sbSizer1811.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer2111.Add( self.m_staticline611, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        gSizer911.Add( bSizer2111, 1, wx.EXPAND, 5 )
        
        bSizer2211 = wx.BoxSizer( wx.VERTICAL )
        
        self.Entrada_Limpia1 = wx.TextCtrl( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"Ejemplo C:/User/Desktop/Mi_Carpeta_Base", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2211.Add( self.Entrada_Limpia1, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer911.Add( bSizer2211, 1, wx.EXPAND, 5 )
        
        bSizer2311 = wx.BoxSizer( wx.VERTICAL )
        
        self.Evaluacion_Limpia1 = wx.TextCtrl( sbSizer1811.GetStaticBox(), wx.ID_ANY, u"Ejemplo C:/User/Desktop/Mi_Carpeta_Evaluacion", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2311.Add( self.Evaluacion_Limpia1, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer911.Add( bSizer2311, 1, wx.EXPAND, 5 )
        
        
        sbSizer1811.Add( gSizer911, 1, wx.EXPAND, 5 )
        
        
        bSizer14.Add( sbSizer1811, 1, wx.EXPAND, 5 )
        
        
        gSizer7.Add( bSizer14, 1, wx.EXPAND, 5 )
        
        bSizer16 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer181 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Vector de los archivos del modelo" ), wx.VERTICAL )
        
        gSizer33 = wx.GridSizer( 2, 1, 0, 0 )
        
        bSizer109 = wx.BoxSizer( wx.VERTICAL )
        
        self.Vector_Modelo = wx.TextCtrl( sbSizer181.GetStaticBox(), wx.ID_ANY, u"Aqui va salir parte del vector", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer109.Add( self.Vector_Modelo, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        gSizer33.Add( bSizer109, 1, wx.EXPAND, 5 )
        
        bSizer111 = wx.BoxSizer( wx.VERTICAL )
        
        self.Descripcion_modelo_vector = wx.TextCtrl( sbSizer181.GetStaticBox(), wx.ID_ANY, u"Aparecera un informacion que describe el vector", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer111.Add( self.Descripcion_modelo_vector, 1, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        
        gSizer33.Add( bSizer111, 1, wx.EXPAND, 5 )
        
        
        sbSizer181.Add( gSizer33, 1, wx.EXPAND, 5 )
        
        
        bSizer16.Add( sbSizer181, 1, wx.EXPAND, 5 )
        
        
        gSizer7.Add( bSizer16, 1, wx.EXPAND, 5 )
        
        bSizer18 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer1812 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Vector de los archivos de prueba del modelo" ), wx.VERTICAL )
        
        gSizer331 = wx.GridSizer( 2, 1, 0, 0 )
        
        bSizer1091 = wx.BoxSizer( wx.VERTICAL )
        
        self.Vector_Modelo_Prueba = wx.TextCtrl( sbSizer1812.GetStaticBox(), wx.ID_ANY, u"Aqui va salir parte del vector", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1091.Add( self.Vector_Modelo_Prueba, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
        
        
        gSizer331.Add( bSizer1091, 1, wx.EXPAND, 5 )
        
        bSizer1111 = wx.BoxSizer( wx.VERTICAL )
        
        self.Descripcion_modelo_vector_prueba = wx.TextCtrl( sbSizer1812.GetStaticBox(), wx.ID_ANY, u"Aparecera un informacion que describe el vector", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1111.Add( self.Descripcion_modelo_vector_prueba, 1, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        
        gSizer331.Add( bSizer1111, 1, wx.EXPAND, 5 )
        
        
        sbSizer1812.Add( gSizer331, 1, wx.EXPAND, 5 )
        
        
        bSizer18.Add( sbSizer1812, 1, wx.EXPAND, 5 )
        
        
        gSizer7.Add( bSizer18, 1, wx.EXPAND, 5 )
        
        bSizer19 = wx.BoxSizer( wx.VERTICAL )
        
        gSizer14 = wx.GridSizer( 1, 3, 0, 0 )
        
        bSizer40 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Estado del programa" ), wx.VERTICAL )
        
        self.Porcentaje = wx.TextCtrl( sbSizer23.GetStaticBox(), wx.ID_ANY, u"Esperando ejecucion", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer23.Add( self.Porcentaje, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.Barrita = wx.Gauge( sbSizer23.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.Barrita.SetValue( 0 ) 
        sbSizer23.Add( self.Barrita, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer40.Add( sbSizer23, 1, wx.EXPAND, 5 )
        
        
        gSizer14.Add( bSizer40, 1, wx.EXPAND, 5 )
        
        bSizer41 = wx.BoxSizer( wx.VERTICAL )
        
        self.Iniciar_Proceso = wx.Button( self, wx.ID_ANY, u"Iniciar proceso", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer41.Add( self.Iniciar_Proceso, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        
        gSizer14.Add( bSizer41, 1, wx.EXPAND, 5 )
        
        bSizer42 = wx.BoxSizer( wx.VERTICAL )
        
        self.Siguiente_proceso = wx.Button( self, wx.ID_ANY, u"Siguiente proceso", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer42.Add( self.Siguiente_proceso, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer14.Add( bSizer42, 1, wx.EXPAND, 5 )
        
        
        bSizer19.Add( gSizer14, 1, wx.EXPAND, 5 )
        
        
        gSizer7.Add( bSizer19, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( gSizer7 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_MENU, self.Limpiar_texto, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.Vectorizacion_modelo, id = self.m_menuItem2.GetId() )
        self.Bind( wx.EVT_MENU, self.Valor_numerico_vector, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.Generar_modelo, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.Clasificar, id = self.m_menuItem5.GetId() )
        self.Bind( wx.EVT_MENU, self.Especificaciones_modelo, id = self.m_menuItem6.GetId() )
        self.Bind( wx.EVT_MENU, self.Teoria_basica, id = self.m_menuItem7.GetId() )
        self.Bind( wx.EVT_MENU, self.Contacto, id = self.m_menuItem8.GetId() )
        self.Iniciar_Proceso.Bind( wx.EVT_BUTTON, self.Iniciar )
        self.Siguiente_proceso.Bind( wx.EVT_BUTTON, self.next )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def Limpiar_texto( self, event ):
        Seleccion_de_Ventanas(1)
        self.Destroy()
    
    def Vectorizacion_modelo( self, event ):
        Seleccion_de_Ventanas(2)
        self.Destroy()
    
    def Valor_numerico_vector( self, event ):
        Seleccion_de_Ventanas(3)
        self.Destroy()
    
    def Generar_modelo( self, event ):
        Seleccion_de_Ventanas(4)
        self.Destroy()
    
    def Clasificar( self, event ):
        Seleccion_de_Ventanas(5)
        self.Destroy()
    
    def Especificaciones_modelo( self, event ):
        Seleccion_de_Ventanas(6)
        self.Destroy()
    
    def Teoria_basica( self, event ):
        Seleccion_de_Ventanas(7)
        self.Destroy()
    
    def Contacto( self, event ):
        Seleccion_de_Ventanas(8)
        self.Destroy()
    
    def onClose(self,event):
        Mata_Programa_Definitivo(False)
        print j
        self.Destroy()
    
    def Iniciar( self, event ):
        a=self.Entrada_Limpia1.GetValue()
        b=self.Evaluacion_Limpia1.GetValue()
        self.Porcentaje.SetValue("Iniciando")
        self.Barrita.SetValue(10)
        train_files,target = conseguir_todos_los_archivos(a)
        test_files,target2 = conseguir_todos_los_archivos(b)
        self.Porcentaje.SetValue("Iniciando.....")
        self.Barrita.SetValue(50)
        train_data,test_data = read_corpus(train_files,test_files)
        self.Porcentaje.SetValue("Ya casi.....")
        self.Barrita.SetValue(60)
        self.Vector_Modelo.SetValue(train_data[0])
        self.Descripcion_modelo_vector.SetValue("Dimension de vector "+str(len(train_data)))
        self.Vector_Modelo_Prueba.SetValue(test_data[0])
        self.Descripcion_modelo_vector_prueba.SetValue("Dimension de vector "+str(len(test_data)))
        
        pickle.dump( train_data, open( "save1.p", "wb" ) )
        pickle.dump( test_data, open( "save2.p", "wb" ) )
        pickle.dump( target, open( "save3.p", "wb" ) )
        pickle.dump( target2, open( "save4.p", "wb" ) )
        self.Porcentaje.SetValue("Terminado")
        self.Barrita.SetValue(100)
        event.Skip()
    
    def next( self, event ):
        Seleccion_de_Ventanas(3)
        self.Destroy()
'''
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$                        Funcion Principal                                                   $$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
'''
if __name__ == '__main__':
    app = wx.App()
    while j:
        if i==1:
            fr= Objeto1(None)
        elif i==2:
            fr=Objeto2(None)
        app.MainLoop(None)
    pass
    